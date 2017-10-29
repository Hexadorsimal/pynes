from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Write, RW, AddressBus, Increment
from ..addressing_modes import *
from .instruction import Instruction


class Stx(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Write('X'), RW(0)]))
        self.cycles.append(Cycle([RW(1), AddressBus('PCX'), Increment('PCL')]))

        self.addressing_modes = {
            0x86: ZeroPageAddressing,
            0x96: ZeroPageYAddressing,
            0x8E: AbsoluteAddressing,
        }

    @property
    def name(self):
        return 'STX'

    @property
    def description(self):
        return 'Store Index X in Memory'
