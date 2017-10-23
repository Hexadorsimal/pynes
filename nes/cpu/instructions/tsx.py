from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import MoveMicroinstruction
from .implied_instruction import ImpliedInstruction


class Tsx(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveMicroinstruction('S', 'X')]))

    @property
    def name(self):
        return 'TSX'

    @property
    def opcode(self):
        return 0xBA

    @property
    def description(self):
        return 'Transfer Stack Pointer to Index X'
