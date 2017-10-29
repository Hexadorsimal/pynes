from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Move, AddressBus, Read, RW, Increment
from ..addressing_modes import *
from .instruction import Instruction


class Ldx(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Read('X'), AddressBus('PCX'), RW(1), Increment('PCL')]))

        self.addressing_modes = {
            0xA2: ImmediateAddressing,
            0xA6: ZeroPageAddressing,
            0xB6: ZeroPageYAddressing,
            0xAE: AbsoluteAddressing,
            0xBE: AbsoluteYAddressing,
        }

    @property
    def name(self):
        return 'LDX'

    @property
    def description(self):
        return 'Load Index X with Memory'
