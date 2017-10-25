from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Increment, Read, AddressBus, Move
from nes.memory import AbsoluteAddress
from .addressing_mode import AddressingMode


class AbsoluteAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Read(), AddressBus(AbsoluteAddress('PCH', 'PCL')), Increment('PCL')]))
        self.cycles.append(Cycle([Move('DL', 'IR'), Read(), AddressBus(AbsoluteAddress('PCH', 'PCL')), Increment('PCL')]))
        self.cycles.append(Cycle([Move('DL', 'ADL'), Read(), AddressBus(AbsoluteAddress('PCH', 'PCL')), Increment('PCL')]))
        self.cycles.append(Cycle([Move('DL', 'ADH'), Read(), AddressBus(AbsoluteAddress('ADH', 'ADL'))]))

    @property
    def size(self):
        return 3
