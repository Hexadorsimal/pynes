from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Decrement
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Dex(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Decrement('X')]))
        self.addressing_modes = {
            0xCA: ImpliedAddressing
        }

    @property
    def name(self):
        return 'DEX'

    @property
    def description(self):
        return 'Decrement Index X by One'
