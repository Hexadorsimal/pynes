from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import RW, Increment
from nes.memory import AbsoluteAddress, StackAddress
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Rti(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([RW(1), (AbsoluteAddress('PCH', 'PCL'), 'IR')]))
        self.cycles.append(Cycle([RW(1), (StackAddress('S'), 'DL'), Increment('S')]))
        self.cycles.append(Cycle([RW(1), (StackAddress('S'), 'P'), Increment('S')]))
        self.cycles.append(Cycle([RW(1), (StackAddress('S'), 'PCL'), Increment('S')]))
        self.cycles.append(Cycle([RW(1), (StackAddress('S'), 'PCH')]))
        self.cycles.append(Cycle([RW(1), (AbsoluteAddress('PCH', 'PCL'), 'IR'), Increment('PCL')]))
        self.addressing_modes = {
            0x40: ImpliedAddressing
        }

    @property
    def name(self):
        return 'RTI'

    @property
    def description(self):
        return 'Return from Interrupt'
