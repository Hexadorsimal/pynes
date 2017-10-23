from nes.cpu.cycle import Cycle
from nes.cpu.microinstructions import IncrementMicroinstruction, ReadMicroinstruction
from nes.memory import AbsoluteAddress
from .instruction import Instruction


class AbsoluteInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'ADL'), IncrementMicroinstruction('PCL')]))
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'ADH'), IncrementMicroinstruction('PCL')]))
        self.cycles.append(Cycle([ReadMicroinstruction(AbsoluteAddress('ADH', 'ADL'), 'DL')]))

    @property
    def size(self):
        return 3
