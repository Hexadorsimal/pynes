from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Add
from ..addressing_modes import *
from .instruction import Instruction


class Adc(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Add('A', 'A', 'DL')]))
        self.addressing_modes = {
            0x69: ImmediateAddressing,
            0x65: ZeroPageAddressing,
            0x75: ZeroPageXAddressing,
            0x6D: AbsoluteAddressing,
            0x7D: AbsoluteXAddressing,
            0x79: AbsoluteYAddressing,
            0x61: IndexedIndirectAddressing,
            0x71: IndirectIndexedAddressing,
        }

    @property
    def name(self):
        return 'ADC'

    @property
    def description(self):
        return 'Add Memory to Accumulator with Carry'
