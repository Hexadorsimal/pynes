from ..cycle import Cycle
from ..operation import IncrementOperation, DecrementOperation, ReadOperation, WriteOperation
from ..implied_instruction import ImpliedInstruction
from ...memory.address import AbsoluteAddress, StackAddress


class Pha(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'IR')]))
        self.cycles.append(Cycle([WriteOperation(StackAddress('S'), 'A'), DecrementOperation('S')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'IR'), IncrementOperation('PCL', 'PCH')]))

    @property
    def name(self):
        return 'PHA'

    @property
    def opcode(self):
        return 0x48

    @property
    def description(self):
        return 'Push Accumulator on Stack'
