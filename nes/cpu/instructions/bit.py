from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import BitTest
from ..addressing_modes import *
from .instruction import Instruction


class Bit(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitTest('A', 'DL')]))
        self.addressing_modes = {
            0x24: ZeroPageAddressing,
            0x2C: AbsoluteAddressing,
        }

    @property
    def name(self):
        return 'BIT'

    @property
    def description(self):
        return 'Test Bits in Memory with Accumulator'
