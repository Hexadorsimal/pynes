from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import BitwiseOr
from ..addressing_modes import *
from .instruction import Instruction


class Ora(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([BitwiseOr('A', 'A', 'DL')]))
        self.addressing_modes = {
            0x09: ImmediateAddressing,
            0x05: ZeroPageAddressing,
            0x15: ZeroPageXAddressing,
            0x0D: AbsoluteAddressing,
            0x1D: AbsoluteXAddressing,
            0x19: AbsoluteYAddressing,
            0x01: IndexedIndirectAddressing,
            0x11: IndirectIndexedAddressing,
        }

    @property
    def name(self):
        return 'ORA'

    @property
    def description(self):
        return 'OR Memory with Accumulator'
