from ..cycle import Cycle
from ..operation import Operation
from ..implied_instruction import ImpliedInstruction


class BreakOperation(Operation):
    def __init__(self):
        super().__init__()

    def execute(self, processor):
        pass


class Brk(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BreakOperation()]))

    @property
    def name(self):
        return 'BRK'

    @property
    def opcode(self):
        return 0x00

    @property
    def description(self):
        return 'Force Break'
