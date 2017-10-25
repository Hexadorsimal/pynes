from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import BitwiseAnd
from ..addressing_modes import *
from .instruction import Instruction


class And(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseAnd('A', 'A', 'DL')]))
        self.variants = {
            0x29: ImmediateAddressing,
            0x25: ZeroPageAddressing,
            0x35: ZeroPageXAddressing,
            0x2D: AbsoluteAddressing,
            0x3D: AbsoluteXAddressing,
            0x39: AbsoluteYAddressing,
            0x21: IndexedIndirectAddressing,
            0x31: IndirectIndexedAddressing,
        }

    @property
    def name(self):
        return 'AND'

    @property
    def opcode(self):
        return 0x29

    @property
    def description(self):
        return 'AND Memory with Accumulator'
