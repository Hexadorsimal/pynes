from ..cycle import Cycle
from ..operation import MoveOperation
from ..implied_instruction import ImpliedInstruction


class Tya(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('Y', 'A')]))

    @property
    def name(self):
        return 'TYA'

    @property
    def opcode(self):
        return 0x98

    @property
    def description(self):
        return 'Transfer Index Y to Accumulator'
