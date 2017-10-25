from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import AddressBus, Read, Increment
from nes.memory import AbsoluteAddress, StackAddress
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Rts(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddressBus(AbsoluteAddress('PCH', 'PCL')), Read()]))
        self.cycles.append(Cycle([AddressBus(StackAddress('S')), Read(), Increment('S')]))
        self.cycles.append(Cycle([AddressBus(StackAddress('S')), Read(), Increment('S')]))
        self.cycles.append(Cycle([AddressBus(StackAddress('S')), Read()]))
        self.cycles.append(Cycle([AddressBus(AbsoluteAddress('PCH', 'PCL')), Read(), Increment('PCL')]))
        self.cycles.append(Cycle([AddressBus(AbsoluteAddress('PCH', 'PCL')), Read(), Increment('PCL')]))
        self.addressing_modes = {
            0x60: ImpliedAddressing
        }

    @property
    def name(self):
        return 'RTS'

    @property
    def description(self):
        return 'Return from Subroutine'
