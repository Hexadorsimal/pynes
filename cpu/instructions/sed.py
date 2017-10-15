from ..cycle import Cycle
from ..operation import SetFlagOperation
from ..implied_instruction import ImpliedInstruction


class SetDecimalFlagOperation(SetFlagOperation):
    def __init__(self):
        super().__init__('D')


class Cld(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([SetDecimalFlagOperation()]))

    @property
    def name(self):
        return 'SED'

    @property
    def opcode(self):
        return 0xF8

    @property
    def description(self):
        return 'Set Decimal Mode'
