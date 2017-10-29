from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import RW, Write, Increment, Decrement
from nes.memory import AbsoluteAddress, StackAddress
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Php(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RW(1), (AbsoluteAddress('PCH', 'PCL'), 'IR')]))
        self.cycles.append(Cycle([RW(0), (StackAddress('S'), 'P'), Decrement('S')]))
        self.cycles.append(Cycle([RW(1), (AbsoluteAddress('PCH', 'PCL'), 'IR'), Increment('PCL')]))
        self.addressing_modes = {
            0x08: ImpliedAddressing
        }

    @property
    def name(self):
        return 'PHP'

    @property
    def description(self):
        return 'Push Processor Status on Stack'
