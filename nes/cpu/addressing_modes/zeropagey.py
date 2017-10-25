from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import ReadMicroinstruction, IncrementMicroinstruction
from nes.memory import AbsoluteAddress, ZeroPageAddress
from .addressing_mode import AddressingMode


class ZeroPageYAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'BAL'), IncrementMicroinstruction('PCL')]))
        self.cycles.append(Cycle([ReadMicroinstruction(ZeroPageAddress('BAL'), 'DL')]))
        self.cycles.append(Cycle([ReadMicroinstruction(ZeroPageAddress('BAL + Y'), 'DL')]))

    @property
    def size(self):
        return 2
