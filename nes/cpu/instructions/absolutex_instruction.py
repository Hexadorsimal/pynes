from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import IncrementMicroinstruction, ReadMicroinstruction
from nes.memory import AbsoluteAddress
from .instruction import Instruction


class AbsoluteXInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'BAL'), IncrementMicroinstruction('PCL')]))
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'BAH'), IncrementMicroinstruction('PCL')]))
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('BAH', 'BAL + X'), 'DL')]))

        # When C = 1
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('BAH + 1', 'BAL + X'), 'DL')]))

    @property
    def size(self):
        return 3
