from ..cycle import Cycle
from ..operation import MoveOperation
from ..implied_instruction import ImpliedInstruction


class Tsx(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveOperation('S', 'X')]))

    @property
    def name(self):
        return 'TSX'

    @property
    def opcode(self):
        return 0xBA

    @property
    def description(self):
        return 'Transfer Stack Pointer to Index X'
