from nes.processors.cpu.instruction import Instruction
from nes.processors.cpu import Cpu


class Jmp(Instruction):
    def execute(self, cpu: Cpu) -> None:
        cpu.pc.value = self.addressing_mode.calculate_address(cpu, self.parameter)
