from pokeretriever import Request
from pokeretriever import PokedexHelper


class Pokedex:
    mode = {"pokemon": 1,
            "ability": 2,
            "move": 3}


def main():
    request = Request()
    request.get_args()
    PokedexHelper.execute_request(request)


if __name__ == "__main__":
    main()
