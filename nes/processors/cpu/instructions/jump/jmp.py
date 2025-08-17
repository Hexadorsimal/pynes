from ..instruction import Instruction
from ... import Cpu


class Jmp(Instruction):
    def execute(self, cpu: Cpu) -> None:
        cpu.pc.value = self.addressing_mode.calculate_address(cpu, self.parameter)
