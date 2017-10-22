from ..alu.alu import AluIncrementOperation
from ..cycle import Cycle
from ..operation import ReadOperation
from ..implied_instruction import ImpliedInstruction
from ...memory.address import AbsoluteAddress, StackAddress


class Rts(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'DL')]))
        self.cycles.append(Cycle([ReadOperation(StackAddress('S'), 'DL'), AluIncrementOperation('S')]))
        self.cycles.append(Cycle([ReadOperation(StackAddress('S'), 'PCL'), AluIncrementOperation('S')]))
        self.cycles.append(Cycle([ReadOperation(StackAddress('S'), 'PCH')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'DL'), AluIncrementOperation('PCL')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'IR'), AluIncrementOperation('PCL')]))

    @property
    def name(self):
        return 'RTS'

    @property
    def opcode(self):
        return 0x60

    @property
    def description(self):
        return 'Return from Subroutine'
