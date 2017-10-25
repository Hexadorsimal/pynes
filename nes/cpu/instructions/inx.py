from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Increment
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Inx(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Increment('X')]))
        self.addressing_modes = {
            0xE8: ImpliedAddressing
        }

    @property
    def name(self):
        return 'INX'

    @property
    def description(self):
        return 'Increment Index X by One'
