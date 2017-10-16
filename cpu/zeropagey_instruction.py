from .cycle import Cycle
from .instruction import Instruction
from .operation import ReadOperation, IncrementOperation


class ZeroPageXInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'BAL'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation(0x00, 'BAL', 'DL')]))
        self.cycles.append(Cycle([ReadOperation(0x00, 'BAL + Y', 'DL')]))

    @property
    def size(self):
        return 2
