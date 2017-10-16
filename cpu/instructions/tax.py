from ..cycle import Cycle
from ..operation import MoveOperation
from ..implied_instruction import ImpliedInstruction


class Tax(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('A', 'X')]))

    @property
    def name(self):
        return 'TAX'

    @property
    def opcode(self):
        return 0xAA

    @property
    def description(self):
        return 'Transfer Accumulator to Index X'
