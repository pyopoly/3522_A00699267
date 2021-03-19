from pokeretriever import Request


class Pokedex:
    mode = {"pokemon": 1,
            "ability": 2,
            "move": 3}


def main():
    request = Request()
    request.get_args()


if __name__ == "__main__":
    main()
