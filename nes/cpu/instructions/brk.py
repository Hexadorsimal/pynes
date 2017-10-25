from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Microinstruction
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class Break(Microinstruction):
    def __init__(self):
        super().__init__()

    def execute(self, processor):
        pass


class Brk(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Break()]))
        self.addressing_modes = {
            0x00: ImpliedAddressing
        }

    @property
    def name(self):
        return 'BRK'

    @property
    def description(self):
        return 'Force Break'
