from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import MoveMicroinstruction
from .implied_instruction import ImpliedInstruction


class Txa(ImpliedInstruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([MoveMicroinstruction('X', 'A')]))

    @property
    def name(self):
        return 'TXA'

    @property
    def opcode(self):
        return 0x8A

    @property
    def description(self):
        return 'Transfer Index X to Accumulator'
