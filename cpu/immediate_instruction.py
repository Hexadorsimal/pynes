from .cycle import Cycle
from .instruction import Instruction
from .operation import ReadOperation, IncrementOperation


class ImmediateInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'DL'), IncrementOperation('PCL', 'PCH')]))

    @property
    def size(self):
        return 2
