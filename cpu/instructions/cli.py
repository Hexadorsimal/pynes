from ..cycle import Cycle
from ..operation import ClearFlagOperation
from ..instruction import Instruction


class CliOperation(ClearFlagOperation):
    def __init__(self):
        super().__init__('I')


class Cli(Instruction):
    def __init__(self):
        super().__init__()
        cycle0 = Cycle([CliOperation()])
        self.cycles.append(cycle0)
