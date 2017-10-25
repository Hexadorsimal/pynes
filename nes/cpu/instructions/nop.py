from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Microinstruction
from ..addressing_modes import ImpliedAddressing
from .instruction import Instruction


class NopMicroinstruction(Microinstruction):
    def __init__(self):
        super().__init__()

    def execute(self, processor):
        pass


class Nop(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([NopMicroinstruction()]))
        self.addressing_modes = {
            0xEA: ImpliedAddressing
        }

    @property
    def name(self):
        return 'NOP'

    @property
    def description(self):
        return 'No Operation'
