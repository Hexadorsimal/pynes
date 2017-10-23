from nes.cpu.cycle import Cycle
from nes.cpu.operations import ReadOperation, IncrementOperation
from nes.memory import AbsoluteAddress, ZeroPageAddress
from .instruction import Instruction


class ZeroPageInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'ADL'), IncrementOperation('PCL')]))
        self.cycles.append(Cycle([ReadOperation(ZeroPageAddress('ADL'), 'DL')]))

    @property
    def size(self):
        return 2
