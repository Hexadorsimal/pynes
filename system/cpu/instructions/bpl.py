from ..cycle import Cycle
from ..operation import BranchOperation
from ..relative_instruction import RelativeInstruction


class Bpl(RelativeInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BranchOperation('N', False)]))

    @property
    def name(self):
        return 'BPL'

    @property
    def opcode(self):
        return 0x10

    @property
    def description(self):
        return 'Branch on Result Plus'
