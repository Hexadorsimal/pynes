from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import ClearFlag
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Cli(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ClearFlag('I')]))
        self.addressing_modes = {
            0x58: ImpliedAddressing
        }

    @property
    def name(self):
        return 'CLI'

    @property
    def description(self):
        return 'Clear Interrupt Disable Bit'
