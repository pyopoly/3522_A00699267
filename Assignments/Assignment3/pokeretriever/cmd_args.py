import argparse

class CmdArgs:
    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description="My Pokedex")
        parser.add_argument("mode", choices=['pokemon', 'ability', 'move'])
        # exclusive
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--inputfile')
        group.add_argument('--inputdata')
        # Optional
        parser.add_argument("--expanded", action='store_true')
        parser.add_argument("--output")
        args = parser.parse_args()
        print(args)
        return args
