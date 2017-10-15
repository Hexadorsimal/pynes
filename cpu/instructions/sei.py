from ..cycle import Cycle
from ..operation import SetFlagOperation
from ..implied_instruction import ImpliedInstruction


class SetInterruptDisableBitOperation(SetFlagOperation):
    def __init__(self):
        super().__init__('I')


class Sei(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([SetInterruptDisableBitOperation()]))

    @property
    def name(self):
        return 'SEI'

    @property
    def opcode(self):
        return 0x78

    @property
    def description(self):
        return 'Set Interrupt Disable Status'
