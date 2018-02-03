from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Read, AluPassthrough, AddressBus, RW, Increment
from ..addressing_modes import *
from .instruction import Instruction


class Lda(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Read('A'), AluPassthrough('A'), AddressBus('PCX'), RW(1), Increment('PCL')]))
        self.addressing_modes = {
            0xA9: ImmediateAddressing,
            0xA5: ZeroPageAddressing,
            0xB5: ZeroPageXAddressing,
            0xAD: AbsoluteAddressing,
            0xBD: AbsoluteXAddressing,
            0xB9: AbsoluteYAddressing,
            0xA1: IndexedIndirectAddressing,
            0xB1: IndirectIndexedAddressing,
        }

    @property
    def name(self):
        return 'LDA'

    @property
    def description(self):
        return 'Load Accumulator with Memory'
