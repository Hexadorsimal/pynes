from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Subtract
from ..addressing_modes import *
from .instruction import Instruction


class Sbc(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Subtract('A', 'A', 'DL')]))
        self.addressing_modes = {
            0xE9: ImmediateAddressing,
            0xE5: ZeroPageAddressing,
            0xF5: ZeroPageXAddressing,
            0xED: AbsoluteAddressing,
            0xFD: AbsoluteXAddressing,
            0xF9: AbsoluteYAddressing,
            0xE1: IndexedIndirectAddressing,
            0xF1: IndirectIndexedAddressing,
        }

    @property
    def name(self):
        return 'SBC'

    @property
    def description(self):
        return 'Subtract Memory from Accumulator with Borrow'
