from ..cycle import Cycle
from ..operation import ClearFlagOperation
from ..implied_instruction import ImpliedInstruction


class ClearCarryFlagOperation(ClearFlagOperation):
    def __init__(self):
        super().__init__('C')


class Clc(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ClearCarryFlagOperation()]))

    @property
    def name(self):
        return 'CLC'

    @property
    def opcode(self):
        return 0x18

    @property
    def description(self):
        return 'Clear Carry Flag'
