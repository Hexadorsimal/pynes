from ..cycle import Cycle
from ..operation import BranchOperation
from ..relative_instruction import RelativeInstruction


class Bmi(RelativeInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BranchOperation('N', True)]))

    @property
    def name(self):
        return 'BMI'

    @property
    def opcode(self):
        return 0x30

    @property
    def description(self):
        return 'Branch on Result Minus'
