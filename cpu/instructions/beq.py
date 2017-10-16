from ..cycle import Cycle
from ..operation import BranchOperation
from ..relative_instruction import RelativeInstruction


class Beq(RelativeInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BranchOperation('Z', True)]))

    @property
    def name(self):
        return 'BEQ'

    @property
    def opcode(self):
        return 0xF0

    @property
    def description(self):
        return 'Branch on Result Zero'
