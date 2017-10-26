from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import AddressBusSelect, Read, Increment
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Rts(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddressBusSelect('PCX'), Read()]))
        self.cycles.append(Cycle([AddressBusSelect('STACK'), Read(), Increment('S')]))
        self.cycles.append(Cycle([AddressBusSelect('STACK'), Read(), Increment('S')]))
        self.cycles.append(Cycle([AddressBusSelect('STACK'), Read()]))
        self.cycles.append(Cycle([AddressBusSelect('PCX'), Read(), Increment('PCL')]))
        self.cycles.append(Cycle([AddressBusSelect('PCX'), Read(), Increment('PCL')]))
        self.addressing_modes = {
            0x60: ImpliedAddressing
        }

    @property
    def name(self):
        return 'RTS'

    @property
    def description(self):
        return 'Return from Subroutine'
