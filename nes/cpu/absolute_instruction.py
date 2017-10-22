from .alu.alu import AluIncrementOperation
from .cycle import Cycle
from .instruction import Instruction
from .operation import ReadOperation
from ..memory.address import AbsoluteAddress


class AbsoluteInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'ADL'), AluIncrementOperation('PCL')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'ADH'), AluIncrementOperation('PCL')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('ADH', 'ADL'), 'DL')]))

    @property
    def size(self):
        return 3
