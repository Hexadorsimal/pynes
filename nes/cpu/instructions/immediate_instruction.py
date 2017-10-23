from nes.cpu.cycle import Cycle
from nes.cpu.operations import IncrementOperation, ReadOperation
from nes.memory import AbsoluteAddress
from .instruction import Instruction


class ImmediateInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'DL'), IncrementOperation('PCL')]))

    @property
    def size(self):
        return 2
