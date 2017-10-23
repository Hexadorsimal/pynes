from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import ReadMicroinstruction, IncrementMicroinstruction
from nes.memory import AbsoluteAddress, ZeroPageAddress
from .instruction import Instruction


class ZeroPageInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'ADL'), IncrementMicroinstruction('PCL')]))
        self.cycles.append(Cycle([ReadMicroinstruction(ZeroPageAddress('ADL'), 'DL')]))

    @property
    def size(self):
        return 2
