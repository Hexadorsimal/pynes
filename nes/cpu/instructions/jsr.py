from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Decrement, Increment, Read, Write, RW, AddressBus, Move
from ..addressing_modes import JsrAbsoluteAddressing
from .instruction import Instruction


class Jsr(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([Read('ADL')]))
        self.cycles.append(Cycle([Write('PCH'), AddressBus('STACK'), RW(0), Decrement('S')]))
        self.cycles.append(Cycle([Write('PCL'), AddressBus('STACK'), RW(0), Decrement('S')]))
        self.cycles.append(Cycle([AddressBus('PCX'), RW(1), Increment('PCL')]))
        self.cycles.append(Cycle([Read('ADH'), AddressBus('ADX'), RW(1), Move('ADL', 'PCL'), Move('ADH', 'PCH')]))

        self.addressing_modes = {
            0x20: JsrAbsoluteAddressing
        }

    @property
    def name(self):
        return 'JSR'

    @property
    def description(self):
        return 'Jump to Subroutine'
