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

    def __init__(self):
        self._mode = None
        self._input_filename = None
        self._input_data = None
        self._expanded = False
        self._output_filename = None
        # self._output = False
        # self._input_file = False

    def get_args(self):
        args = CmdArgs.get_args()
        self._mode = args.mode
        self._input_filename = args.inputfile
        self._input_data = args.inputdata
        self._expanded = args.expanded
        self._output_filename = args.output

    @property
    def mode(self):
        return self._mode

    @property
    def input_data(self):
        return self._input_data


    def __str__(self):
        return f"{self._mode}, data: {self._input_data}, input file: {self._input_filename}, " \
               f"expanded: {self._expanded}, output: {self._output_filename}"
