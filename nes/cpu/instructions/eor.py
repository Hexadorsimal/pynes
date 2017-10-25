from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import BitwiseXor
from ..addressing_modes import *
from .instruction import Instruction


class Eor(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseXor('A', 'A', 'DL')]))
        self.addressing_modes = {
            0x49: ImmediateAddressing,
            0x45: ZeroPageAddressing,
            0x55: ZeroPageXAddressing,
            0x4D: AbsoluteAddressing,
            0x5D: AbsoluteXAddressing,
            0x59: AbsoluteYAddressing,
            0x41: IndexedIndirectAddressing,
            0x51: IndirectIndexedAddressing,
        }

    @property
    def name(self):
        return 'EOR'

    @property
    def description(self):
        return 'Exclusive OR Memory with Accumulator'
