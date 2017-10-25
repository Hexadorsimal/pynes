from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import ClearFlag
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Clc(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ClearFlag('C')]))
        self.addressing_modes = {
            0x18: ImpliedAddressing
        }

    @property
    def name(self):
        return 'CLC'

    @property
    def description(self):
        return 'Clear Carry Flag'
