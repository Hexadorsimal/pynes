from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Decrement, Increment, Read, RW, AddressBus, Move
from ..addressing_modes import AbsoluteAddressing
from .instruction import Instruction


class Jsr(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddressBus('PCX'), RW(1), Increment('PCL')]))
        self.cycles.append(Cycle([Move('DL', 'ADL')]))
        self.cycles.append(Cycle([Move('PCH', 'DL'), AddressBus('STACK'), RW(0), Decrement('S')]))
        self.cycles.append(Cycle([Move('PCL', 'DL'), AddressBus('STACK'), RW(0), Decrement('S')]))
        self.cycles.append(Cycle([AddressBus('PCX'), RW(1), Increment('PCL')]))
        self.cycles.append(Cycle([Move('DL', 'ADH'), AddressBus('ADX'), RW(1), Move('ADL', 'PCL'), Move('ADH', 'PCH')]))
        self.addressing_modes = {
            0x20: AbsoluteAddressing
        }

    @property
    def name(self):
        return 'JSR'

    @property
    def description(self):
        return 'Jump to Subroutine'
