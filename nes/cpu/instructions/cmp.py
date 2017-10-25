from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Compare
from ..addressing_modes import *
from .instruction import Instruction


class Cmp(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Compare('A', 'DL')]))
        self.addressing_modes = {
            0xC9: ImmediateAddressing,
            0xC5: ZeroPageAddressing,
            0xD5: ZeroPageXAddressing,
            0xCD: AbsoluteAddressing,
            0xDD: AbsoluteXAddressing,
            0xD9: AbsoluteYAddressing,
            0xC1: IndexedIndirectAddressing,
            0xD1: IndirectIndexedAddressing,
        }

    @property
    def name(self):
        return 'CMP'

    @property
    def description(self):
        return 'Compare Memory and Accumulator'
