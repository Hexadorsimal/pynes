from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Move
from ..addressing_modes import *
from .instruction import Instruction


class Stx(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Move('X', 'DL')], 'write'))
        self.addressing_modes = {
            0x86: ZeroPageAddressing,
            0x96: ZeroPageYAddressing,
            0x8E: AbsoluteAddressing,
        }

    @property
    def name(self):
        return 'STX zpg'

    @property
    def description(self):
        return 'Store Index X in Memory (ZeroPage)'
