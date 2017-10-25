from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Move
from ..addressing_modes import *
from .instruction import Instruction


class Sta(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Move('A', 'DL')]))
        self.addressing_modes = {
            0x85: ZeroPageAddressing,
            0x95: ZeroPageXAddressing,
            0x8D: AbsoluteAddressing,
            0x9D: AbsoluteXAddressing,
            0x99: AbsoluteYAddressing,
            0x81: IndexedIndirectAddressing,
            0x91: IndirectIndexedAddressing,
        }

    @property
    def name(self):
        return 'STA zpg'

    @property
    def description(self):
        return 'Store Accumulator in Memory (ZeroPage)'
