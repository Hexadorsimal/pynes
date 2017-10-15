from ..cycle import Cycle
from ..operation import ClearFlagOperation
from ..implied_instruction import ImpliedInstruction


class ClearOverflowFlagOperation(ClearFlagOperation):
    def __init__(self):
        super().__init__('I')


class Clv(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ClearOverflowFlagOperation()]))

    @property
    def name(self):
        return 'CLV'

    @property
    def opcode(self):
        return 0xB8

    @property
    def description(self):
        return 'Clear Overflow Flag'
