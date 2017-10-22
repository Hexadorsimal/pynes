from .cycle import Cycle
from .instruction import Instruction
from .operation import ReadOperation, IncrementOperation
from ..memory.address import AbsoluteAddress, ZeroPageAddress


class ZeroPageXInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'BAL'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation(ZeroPageAddress('BAL'), 'DL')]))
        self.cycles.append(Cycle([ReadOperation(ZeroPageAddress('BAL + X'), 'DL')]))

    @property
    def size(self):
        return 2
