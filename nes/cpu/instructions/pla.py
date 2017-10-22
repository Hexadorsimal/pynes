from ..cycle import Cycle
from ..operation import IncrementOperation, ReadOperation, WriteOperation
from ..implied_instruction import ImpliedInstruction
from ...memory.address import AbsoluteAddress, StackAddress


class Pla(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'IR')]))
        self.cycles.append(Cycle([WriteOperation(StackAddress('S'), 'DL'), IncrementOperation('S')]))
        self.cycles.append(Cycle([WriteOperation(StackAddress('S'), 'A')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'IR'), IncrementOperation('PCL', 'PCH')]))

    @property
    def name(self):
        return 'PLA'

    @property
    def opcode(self):
        return 0x68

    @property
    def description(self):
        return 'Pull Accumulator from Stack'
