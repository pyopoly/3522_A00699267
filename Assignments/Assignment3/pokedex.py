from pokeretriever import Request
from pokeretriever import PokedexHelper


# class Pokedex:


def main():
    request = Request()
    request.get_args()
    pokedex_object = PokedexHelper.execute_request(request)
    print(pokedex_object)

if __name__ == "__main__":
    main()
