from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Read, AluPassthrough, AddressBus, RW, Increment
from ..addressing_modes import *
from .instruction import Instruction


class Ldy(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Read('Y'), AluPassthrough('Y'), AddressBus('PCX'), RW(1), Increment('PCL')]))
        self.addressing_modes = {
            0xA0: ImmediateAddressing,
            0xA4: ZeroPageAddressing,
            0xB4: ZeroPageXAddressing,
            0xAC: AbsoluteAddressing,
            0xBC: AbsoluteYAddressing,
        }

    @property
    def name(self):
        return 'LDY'

    @property
    def description(self):
        return 'Load Index Y with Memory'
