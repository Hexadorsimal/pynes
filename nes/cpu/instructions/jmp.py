from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Move, Read, AddressBusSelect
from ..addressing_modes import *
from .instruction import Instruction


class Jmp(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Move('ADL', 'PCL'), Move('DL', 'PCH'), AddressBusSelect('PCX'), Read()]))

        self.addressing_modes = {
            0x4C: JumpAbsoluteAddressing,
            0x6C: IndirectAbsoluteAddressing,
        }

    @property
    def name(self):
        return 'JMP'

    @property
    def description(self):
        return 'Jump to New Location'
