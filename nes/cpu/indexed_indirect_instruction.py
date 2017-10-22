from .alu.alu import AluIncrementOperation
from .cycle import Cycle
from .instruction import Instruction
from .operation import ReadOperation
from ..memory.address import AbsoluteAddress, ZeroPageAddress


class IndexedIndirectInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'BAL'), AluIncrementOperation('PCL')]))
        self.cycles.append(Cycle([ReadOperation(ZeroPageAddress('BAL'), 'DL')]))
        self.cycles.append(Cycle([ReadOperation(ZeroPageAddress('BAL + X'), 'ADL')]))
        self.cycles.append(Cycle([ReadOperation(ZeroPageAddress('BAL + X + 1'), 'ADH')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('ADH', 'ADL'), 'DL')]))

    @property
    def size(self):
        return 2
