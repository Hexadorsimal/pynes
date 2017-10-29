from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import Increment, Read, AddressBus, RW
from .addressing_mode import AddressingMode


class AbsoluteAddressing(AddressingMode):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([AddressBus('PCX'), RW(1), Increment('PCL')]))
        self.cycles.append(Cycle([Read('ADL'), AddressBus('PCX'), RW(1), Increment('PCL')]))
        self.cycles.append(Cycle([Read('ADH'), AddressBus('ADX'), RW(1)]))

    @property
    def size(self):
        return 3


class JmpAbsoluteAddressing(AbsoluteAddressing):
    def __init__(self):
        super().__init__()

        # JMP is the only Absolute Addressing mode instruction that skips the last step of that mode
        self.cycles.pop()


class JsrAbsoluteAddressing(JmpAbsoluteAddressing):
    def __init__(self):
        super().__init__()

        self.cycles.pop()
