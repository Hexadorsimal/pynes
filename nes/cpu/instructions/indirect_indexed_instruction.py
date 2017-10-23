from nes.cpu.cycle import Cycle
from nes.cpu.operations import IncrementOperation ,ReadOperation
from nes.memory import AbsoluteAddress, ZeroPageAddress
from .instruction import Instruction


class IndirectIndexedInstruction(Instruction):
    def __init__(self):
        super().__init__()
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'IAL'), IncrementOperation('PCL')]))
        self.cycles.append(Cycle([ReadOperation(ZeroPageAddress('IAL'), 'BAL')]))
        self.cycles.append(Cycle([ReadOperation(ZeroPageAddress('IAL + 1'), 'BAH')]))
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('BAH', 'BAL + Y'), 'DL')]))

        # when C = 1 or read-modify-write or STA
        self.cycles.append(Cycle([ReadOperation(AbsoluteAddress('BAH + 1', 'BAL + Y'), 'DL')]))

    @property
    def size(self):
        return 2
