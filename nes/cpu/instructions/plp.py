from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import RW, Increment
from nes.memory import AbsoluteAddress, StackAddress
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Plp(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RW(1), (AbsoluteAddress('PCH', 'PCL'), 'IR')]))
        self.cycles.append(Cycle([RW(0), (StackAddress('S'), 'DL'), Increment('S')]))
        self.cycles.append(Cycle([RW(0), (StackAddress('S'), 'P')]))
        self.cycles.append(Cycle([RW(1), (AbsoluteAddress('PCH', 'PCL'), 'IR'), Increment('PCL')]))
        self.addressing_modes = {
            0x28: ImpliedAddressing
        }

    @property
    def name(self):
        return 'PLP'

    @property
    def description(self):
        return 'Pull Processor Status from Stack'
