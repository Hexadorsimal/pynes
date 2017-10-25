from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Decrement
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Dey(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Decrement('Y')]))
        self.addressing_modes = {
            0x88: ImpliedAddressing
        }

    @property
    def name(self):
        return 'DEY'

    @property
    def description(self):
        return 'Decrement Index Y by One'
