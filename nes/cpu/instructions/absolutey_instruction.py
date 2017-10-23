from nes.cpu.cycle import Cycle
from nes.cpu.operations import IncrementOperation, ReadOperation
from nes.memory import AbsoluteAddress
from .instruction import Instruction


class AbsoluteYInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'BAL'), IncrementOperation('PCL')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'BAH'), IncrementOperation('PCL')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('BAH', 'BAL + Y'), 'DL')]))

        # When C = 1
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('BAH + 1', 'BAL + Y'), 'DL')]))

    @property
    def size(self):
        return 3
