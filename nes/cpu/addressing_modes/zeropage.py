from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Move, Read, Increment
from nes.memory import AbsoluteAddress
from .addressing_mode import AddressingMode


class ZeroPageAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Move('0', 'ADH'),
                                  Read(AbsoluteAddress('PCH', 'PCL'), 'ADL'),
                                  Increment('PCL')]))

    @property
    def size(self):
        return 2
