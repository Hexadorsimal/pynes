from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Read, Increment
from nes.memory import AbsoluteAddress, ZeroPageAddress
from .addressing_mode import AddressingMode


class ZeroPageYAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Read(AbsoluteAddress('PCH', 'PCL'), 'BAL'), Increment('PCL')]))
        self.cycles.append(Cycle([Read(ZeroPageAddress('BAL'), 'DL')]))
        self.cycles.append(Cycle([Read(ZeroPageAddress('BAL + Y'), 'DL')]))

    @property
    def size(self):
        return 2
