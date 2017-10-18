from ..cycle import Cycle
from ..operation import BranchOperation
from ..relative_instruction import RelativeInstruction


class Bne(RelativeInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BranchOperation('Z', False)]))

    @property
    def name(self):
        return 'BNE'

    @property
    def opcode(self):
        return 0xD0

    @property
    def description(self):
        return 'Branch on Result not Zero'
