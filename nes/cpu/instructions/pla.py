from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Read, Write, Increment
from nes.memory import AbsoluteAddress, StackAddress
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Pla(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Read(), (AbsoluteAddress('PCH', 'PCL'), 'IR')]))
        self.cycles.append(Cycle([Write(), (StackAddress('S'), 'DL'), Increment('S')]))
        self.cycles.append(Cycle([Write(), (StackAddress('S'), 'A')]))
        self.cycles.append(Cycle([Read(), (AbsoluteAddress('PCH', 'PCL'), 'IR'), Increment('PCL')]))
        self.addressing_modes = {
            0x68: ImpliedAddressing
        }

    @property
    def name(self):
        return 'PLA'

    @property
    def description(self):
        return 'Pull Accumulator from Stack'
