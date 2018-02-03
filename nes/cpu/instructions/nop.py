from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import AddressBus, RW, Increment
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Nop(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddressBus('PCX'), RW(1), Increment('PCL')]))
        self.addressing_modes = {
            0xEA: ImpliedAddressing
        }

    @property
    def name(self):
        return 'NOP'

    @property
    def description(self):
        return 'No Operation'
