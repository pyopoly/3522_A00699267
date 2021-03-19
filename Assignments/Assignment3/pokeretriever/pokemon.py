"""
Implement a facade class that will provide a simplified interface to the pokeretriever package.
Your program must control access to the package via the interface defined in this facade class.
"""
if __name__ == '__main__':
    from cmd_args import CmdArgs
else:
    from pokeretriever.cmd_args import CmdArgs

class Request:
    """
    Request is a class that contains all the data gathered by the argparse module.
    """
    def __init__(self):
        self._mode = None
        self._expanded = False
        self._output = False
        self._output_filename = ""
        self._input_filename = ""
        self._input_file = False
        self._input_data = False

    def get_args(self):
        args = CmdArgs.get_args()


class PokedexObject:
    """
    PokedexObject is a base class that defines the name and id parameter.
    The Pokemon , Moves , Stat , and Ability classes should inherit from this class.
    """
    pass


class Pokedex:
    @staticmethod
    def execute_request(request: Request) -> PokedexObject:
        pass


class Pokemon:
    pass


class Moves:
    pass


class Stat:
    pass


class Ability:
    pass
