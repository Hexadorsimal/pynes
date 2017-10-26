from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Read, Increment
from nes.memory import AbsoluteAddress
from .addressing_mode import AddressingMode


class RelativeAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Read(), (AbsoluteAddress('PCH', 'PCL'), 'DL'), Increment('PCL')]))

    @property
    def size(self):
        return 2
