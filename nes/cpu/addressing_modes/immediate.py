from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Increment, Read, AddressBus
from nes.memory import AbsoluteAddress
from .addressing_mode import AddressingMode


class ImmediateAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Read(), AddressBus(AbsoluteAddress('PCH', 'PCL')), Increment('PCL')]))

    @property
    def size(self):
        return 2
