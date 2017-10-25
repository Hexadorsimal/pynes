from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import MoveMicroinstruction, ReadMicroinstruction, IncrementMicroinstruction
from nes.memory import AbsoluteAddress
from .addressing_mode import AddressingMode


class ZeroPageAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveMicroinstruction('0', 'ADH'),
                                  ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'ADL'),
                                  IncrementMicroinstruction('PCL')]))

    @property
    def size(self):
        return 2
