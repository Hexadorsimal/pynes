from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Move
from ..addressing_modes import *
from .instruction import Instruction


class Jmp(Instruction):
    def __init__(self):
        super().__init__()

        # JMP is the only Absolute Addressing mode instruction that skips the last step of that mode
        # self.cycles.pop()

        self.cycles.append(Cycle([Move('ADL', 'PCL')]))
        self.cycles.append(Cycle([Move('ADH', 'PCH')]))

        self.addressing_modes = {
            0x4C: AbsoluteAddressing,
            0x6C: IndirectAbsoluteAddressing,
        }

    @property
    def name(self):
        return 'JMP'

    @property
    def description(self):
        return 'Jump to New Location'
