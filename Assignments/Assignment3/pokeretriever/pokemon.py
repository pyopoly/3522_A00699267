"""
Implement a facade class that will provide a simplified interface to the pokeretriever package.
Your program must control access to the package via the interface defined in this facade class.
"""

if __name__ == '__main__':
    from cmd_args import Request
    from session import Session
else:
    from pokeretriever.cmd_args import Request
    from pokeretriever.session import Session

import abc


class PokedexObject:
    """
    PokedexObject is a base class that defines the name and id parameter.
    The Pokemon , Moves , Stat , and Ability classes should inherit from this class.
    """
    def __init__(self, name, id):
        self._name = name
        self._id = id

    def __str__(self):
        return f"{self.__class__.__name__} {'-'*20} \nname: {self._name} \nid: {self._id}"


class PokedexHelper:
    @staticmethod
    def execute_request(request: Request) -> PokedexObject:
        print(request)
        mode = request.mode
        input_data = request.input_data
        expanded = request.expanded
        return PokedexObjectManager.create_pokedex_object(mode, input_data, expanded)


class Pokemon(PokedexObject):
    def __init__(self, name, id, height, weight, stats, types, abilities, moves):
        super().__init__(name, id)
        self._height = height
        self._weight = weight
        self._stats = stats
        self._types = types
        self._abilities = abilities
        self._moves = moves

    def print_move_list(self):
        result = ''.join(f'{"":10}{pair[0]:15} level learnt: {pair[1]}\n' for pair in self._moves)
        return result

    def __str__(self):
        return super().__str__() + f"\n{'height:':10} {self._height} decimetres " \
                                   f"\n{'weight:':10} {self._weight} hectograms" \
                                   f"\n{'stats:':10} {self._stats} \n{'types:':10} {self._types}" \
                                   f"\n{'abilities:':10} {self._abilities} \nmoves: \n{self.print_move_list()}"


class PokemonStat(PokedexObject):
    def __init__(self, name, value, url, id=None, battle_only=None):
        super().__init__(name, id)
        self._url = url
        self._value = value
        self._battle_only = battle_only

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self._name}: {self._value}"


class PokemonMove(PokedexObject):
    def __init__(self, name, id, generation, accuracy, pp, power, move_type, damage_class, short_effect):
        super().__init__(name, id)
        self._generation = generation
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._move_type = move_type
        self._damage_class = damage_class
        self._short_effect = short_effect

    def __str__(self):
        return super().__str__() + f"\n{'gen:':10} {self._generation} \n{'accuracy:':10} {self._accuracy} " \
                                   f"\n{'pp:':10} {self._pp} \n{'power:':10} {self._power}" \
                                   f"\n{'type:':10} {self._move_type} \n{'dmg class:':10} {self._damage_class}" \
                                   f"\n{'effect:':10} {self._short_effect}"


class PokemonAbility(PokedexObject):
    def __init__(self, name, id, generation, effect, short_effect, pokemon_list):
        super().__init__(name, id)
        self._generation = generation
        self._effect = effect
        self._short_effect = short_effect
        self._pokemon_list = pokemon_list

    def __str__(self):
        return super().__str__() + f"\ngen: {self._generation:10} \neffect: {self._effect:10}... " \
                                   f"\nshort: {self._short_effect:10} \npokemon: {self._pokemon_list}"


class Factory(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def create_pokemon(name_or_id, expanded):
        pass

    @staticmethod
    @abc.abstractmethod
    def create_pokemon_stat(name_or_id, expanded):
        pass

    @staticmethod
    @abc.abstractmethod
    def create_pokemon_ability(name_or_id, expanded):
        pass

    @staticmethod
    @abc.abstractmethod
    def create_pokemon_move(name_or_id, expanded):
        pass


class PokemonFactory(Factory):
    @staticmethod
    def create_pokemon(name_or_id, expanded=False):
        query_type = "pokemon"
        json_data = Session.query_info(query_type, name_or_id)
        name = json_data['name']
        id = json_data['id']
        height = json_data['height']
        weight = json_data['weight']

        # Stat
        stats = json_data['stats']
        stats = ((stat_dict['stat']['name'], stat_dict['base_stat'], stat_dict['stat']['url']) for stat_dict in stats)
        stats = [PokemonStat(name, value, url) for name, value, url in stats]


        types = json_data['types']
        types = [type_dict['type']['name'] for type_dict in types]

        # ability
        abilities = json_data['abilities']
        abilities = [ability_dict['ability']['name'] for ability_dict in abilities]

        # moves
        moves = json_data['moves']
        moves = [(move_dict["move"]["name"], move_dict["version_group_details"][0]["level_learned_at"],
                  move_dict["move"]["url"]) for move_dict in moves]
        moves = [(name, level) for name, level, url in moves]
        return Pokemon(name, id, height, weight, stats, types, abilities, moves)

    @staticmethod
    def create_pokemon_stat(name_or_id, expanded=False):
        pass
        # query_type = "stat"
        # json_data = Session.query_info(query_type, name_or_id)
        # name = json_data['name']
        # id = json_data['id']

    @staticmethod
    def create_pokemon_ability(name_or_id, expanded=False):
        query_type = "ability"
        json_data = Session.query_info(query_type, name_or_id)
        name = json_data['name']
        id = json_data['id']
        generation = json_data['generation']['name']
        effect = json_data['effect_entries'][1]['effect']
        short_effect = json_data['effect_entries'][1]['short_effect']
        pokemon_list = json_data['pokemon']
        pokemon_list = [dict['pokemon']['name'] for dict in pokemon_list]
        return PokemonAbility(name, id, generation, effect, short_effect, pokemon_list)

    @staticmethod
    def create_pokemon_move(name_or_id):
        query_type = "move"
        json_data = Session.query_info(query_type, name_or_id)
        name = json_data['name']
        id = json_data['id']
        generation = json_data['generation']['name']
        accuracy = json_data['accuracy']
        pp = json_data['pp']
        power = json_data['power']
        move_type = json_data['type']['name']
        damage_class = json_data['damage_class']['name']
        short_effect = json_data['effect_entries'][0]['short_effect']
        return PokemonMove(name, id, generation, accuracy, pp, power, move_type, damage_class, short_effect)


class PokedexObjectManager:
    pokemon_request_mapping = {
        "pokemon": PokemonFactory.create_pokemon,
        "move": PokemonFactory.create_pokemon_move,
        "ability": PokemonFactory.create_pokemon_ability
    }

    @staticmethod
    def create_pokedex_object(mode, input_data, expanded=False):
        return PokedexObjectManager.pokemon_request_mapping[mode](input_data, expanded)
