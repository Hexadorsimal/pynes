from ..cycle import Cycle
from ..operation import SetFlagOperation
from ..implied_instruction import ImpliedInstruction


class SetCarryFlagOperation(SetFlagOperation):
    def __init__(self):
        super().__init__('C')


class Sec(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([SetCarryFlagOperation()]))

    @property
    def name(self):
        return 'SEC'

    @property
    def opcode(self):
        return 0x38

    @property
    def description(self):
        return 'Set Carry Flag'
