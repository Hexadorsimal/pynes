from ..cycle import Cycle
from ..operation import ReadOperation, IncrementOperation
from ..implied_instruction import ImpliedInstruction
from ...memory.address import AbsoluteAddress, StackAddress


class Rts(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'DL')]))
        self.cycles.append(Cycle([ReadOperation(StackAddress('S'), 'DL'), IncrementOperation('S')]))
        self.cycles.append(Cycle([ReadOperation(StackAddress('S'), 'PCL'), IncrementOperation('S')]))
        self.cycles.append(Cycle([ReadOperation(StackAddress('S'), 'PCH')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'DL'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'IR'), IncrementOperation('PCL', 'PCH')]))

    @property
    def name(self):
        return 'RTS'

    @property
    def opcode(self):
        return 0x60

    @property
    def description(self):
        return 'Return from Subroutine'
