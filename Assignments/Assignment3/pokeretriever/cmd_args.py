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
        return args


class Request:
    """
    Request is a class that contains all the data gathered by the argparse module.
    """

    def __init__(self, mode, input_data=None, expanded=False):
        self._mode = mode
        self._input_data = input_data
        # self._input_filename = input_file
        self._expanded = expanded
        # self._output_filename = output_file

    @classmethod
    def create_request(cls, args):
        return Request(args.mode, args.inputdata.lower(), args.expanded)

    @property
    def mode(self):
        return self._mode

    @property
    def input_data(self):
        return self._input_data

    @property
    def expanded(self):
        return self._expanded

    def __str__(self):
        return f"{self._mode}, data: {self._input_data}, " \
               f"expanded: {self._expanded}"
