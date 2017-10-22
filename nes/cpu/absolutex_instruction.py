from .cycle import Cycle
from .instruction import Instruction
from .operation import ReadOperation, IncrementOperation
from ..memory.address import AbsoluteAddress


class AbsoluteXInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'BAL'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'BAH'), IncrementOperation('PCL', 'PCH')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('BAH', 'BAL + X'), 'DL')]))

        # When C = 1
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('BAH + 1', 'BAL + X'), 'DL')]))

    @property
    def size(self):
        return 3
