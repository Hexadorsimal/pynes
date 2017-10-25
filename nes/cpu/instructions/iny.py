from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Increment
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Iny(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Increment('Y')]))
        self.addressing_modes = {
            0xC8: ImpliedAddressing
        }

    @property
    def name(self):
        return 'INY'

    @property
    def description(self):
        return 'Increment Index Y by One'
