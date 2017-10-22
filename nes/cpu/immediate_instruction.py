from .alu.alu import AluIncrementOperation
from .cycle import Cycle
from .instruction import Instruction
from .operation import ReadOperation
from ..memory.address import AbsoluteAddress


class ImmediateInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'DL'), AluIncrementOperation('PCL')]))

    @property
    def size(self):
        return 2
