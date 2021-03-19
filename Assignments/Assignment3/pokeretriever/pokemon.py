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
        return f"{self.__class__.__name__}: {self._name}, id: {self._id}"


class PokedexHelper:

    @staticmethod
    def execute_request(request: Request) -> PokedexObject:
        # print(request)
        mode = request.mode
        input_data = request.input_data
        return PokedexObjectManager.create_pokedex_object(mode, input_data)


class Pokemon(PokedexObject):
    def __init__(self, name, id):
        super().__init__(name, id)


class PokemonStat(PokedexObject):
    def __init__(self, name, id, battle_only):
        super().__init__(name, id)
        self._battle_only = battle_only


class PokemonMove(PokedexObject):
    def __init__(self, name, id, generation, accuracy, pp, power, move_type):
        super().__init__(name, id)
        self._generation = generation
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._move_type = move_type


class PokemonAbility(PokedexObject):
    def __init__(self, name, id, generation, effect, short_effect, pokemon_list):
        super().__init__(name, id)
        self._generation = generation
        self._effect = effect
        self._short_effect = short_effect
        self._pokemon_list = pokemon_list

    def __str__(self):
        return super().__str__() + f"\ngen: {self._generation} \neffect: {self._effect[:60]}... " \
                                   f"\nshort: {self._short_effect} \npokemon: {self._pokemon_list}"


class Factory(abc.ABC):
    @abc.abstractmethod
    def create_pokemon(self):
        pass

    @staticmethod
    @abc.abstractmethod
    def create_pokemon_ability(name_or_id):
        pass

    @abc.abstractmethod
    def create_pokemon_move(self):
        pass


class PokemonFactory(Factory):
    def create_pokemon(self):
        return PokemonAbility

    @staticmethod
    def create_pokemon_ability(name_or_id):
        query_type = "ability"
        json_data = Session.query_info(query_type, name_or_id)
        name = json_data['name']
        id = json_data['id']
        generation = json_data['generation']['name']
        effect = json_data['effect_entries'][1]['effect']
        short_effect = json_data['effect_entries'][1]['short_effect']
        pokemon_list = json_data['pokemon']
        pokemon_list = [dict['pokemon']['name'] for dict in pokemon_list]

        # print(ability)
        return PokemonAbility(name, id, generation, effect, short_effect, pokemon_list)

    def create_pokemon_move(self):
        return PokemonAbility


class PokedexObjectManager:
    pokemon_request_mapping = {
        "pokemon": PokemonFactory.create_pokemon,
        "move": PokemonFactory.create_pokemon_move,
        "ability": PokemonFactory.create_pokemon_ability
    }

    @staticmethod
    def create_pokedex_object(mode, input_data):
        return PokedexObjectManager.pokemon_request_mapping[mode](input_data)
