from .cycle import Cycle
from .instruction import Instruction
from .operation import ReadOperation, IncrementOperation


class ZeroPageInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'ADL'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation(0x00, 'ADL', 'DL')]))

    @property
    def size(self):
        return 2
