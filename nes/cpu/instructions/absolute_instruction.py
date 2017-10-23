from nes.cpu.cycle import Cycle
from nes.cpu.operations import IncrementOperation, ReadOperation
from nes.memory import AbsoluteAddress
from .instruction import Instruction


class AbsoluteInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'ADL'), IncrementOperation('PCL')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'ADH'), IncrementOperation('PCL')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('ADH', 'ADL'), 'DL')]))

    @property
    def size(self):
        return 3
