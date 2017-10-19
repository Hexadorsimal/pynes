from .cycle import Cycle
from .instruction import Instruction
from .operation import ReadOperation, IncrementOperation


class IndirectIndexedInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation('PCH', 'PCL', 'IAL'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation(0x00, 'IAL', 'BAL')]))
        self.cycles.append(Cycle([ReadOperation(0x00, 'IAL + 1', 'BAH')]))
        self.cycles.append(Cycle([ReadOperation('BAH', 'BAL + Y', 'DL')]))

        # when C = 1 or read-modify-write or STA
        self.cycles.append(Cycle([ReadOperation('BAH + 1', 'BAL + Y', 'DL')]))

    @property
    def size(self):
        return 2
