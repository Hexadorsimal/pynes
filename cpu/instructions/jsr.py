from ..cycle import Cycle
from ..operation import DecrementOperation, IncrementOperation, ReadOperation, WriteOperation
from ..absolute_instruction import AbsoluteInstruction


class Jsr(AbsoluteInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'ADL'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([]))
        self.cycles.append(Cycle([WriteOperation(0x01, 'S', 'PCH'), DecrementOperation('S')]))
        self.cycles.append(Cycle([WriteOperation(0x01, 'S', 'PCL'), DecrementOperation('S')]))
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'ADH'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation('ADH', 'ADL', 'IR')]))

    @property
    def name(self):
        return 'JSR'

    @property
    def opcode(self):
        return 0x20

    @property
    def description(self):
        return 'Jump to Subroutine'
