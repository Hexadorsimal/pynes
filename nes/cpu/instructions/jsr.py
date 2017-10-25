from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Decrement, Increment, Read, Write
from nes.memory import AbsoluteAddress, StackAddress
from ..addressing_modes import AbsoluteAddressing
from .instruction import Instruction


class Jsr(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Read(), (AbsoluteAddress('PCH', 'PCL'), 'ADL'), Increment('PCL')]))
        self.cycles.append(Cycle([]))
        self.cycles.append(Cycle([Write(), (StackAddress('S'), 'PCH'), Decrement('S')]))
        self.cycles.append(Cycle([Write(), (StackAddress('S'), 'PCL'), Decrement('S')]))
        self.cycles.append(Cycle([Read(), (AbsoluteAddress('PCH', 'PCL'), 'ADH'), Increment('PCL')]))
        self.cycles.append(Cycle([Read(), (AbsoluteAddress('ADH', 'ADL'), 'IR')]))
        self.addressing_modes = {
            0x20: AbsoluteAddressing
        }

    @property
    def name(self):
        return 'JSR'

    @property
    def description(self):
        return 'Jump to Subroutine'
