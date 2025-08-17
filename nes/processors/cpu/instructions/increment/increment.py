from nes.processors.registers import Register
from ..instruction import Instruction
from ... import Cpu


class IncrementInstruction(Instruction):
    def increment_register(self, cpu: Cpu, reg: Register, amount: int = 1) -> None:
        reg.value += amount
        self.update_flags(cpu, reg.value)

    def increment_memory(self, cpu: Cpu, amount: int = 1) -> None:
        value = self.read_source(cpu)
        value += amount
        self.update_flags(cpu, value)
        self.write_result(cpu, value)

    @staticmethod
    def update_flags(cpu: Cpu, value: int) -> None:
        cpu.p.update_zero_flag(value)
        cpu.p.update_negative_flag(value)


class Inc(IncrementInstruction):
    def execute(self, cpu: Cpu) -> None:
        self.increment_memory(cpu)


class Inx(IncrementInstruction):
    def execute(self, cpu: Cpu) -> None:
        self.increment_register(cpu, cpu.x)


class Iny(IncrementInstruction):
    def execute(self, cpu: Cpu) -> None:
        self.increment_register(cpu, cpu.y)


class Dec(IncrementInstruction):
    def execute(self, cpu: Cpu) -> None:
        self.increment_memory(cpu, -1)


class Dex(IncrementInstruction):
    def execute(self, cpu: Cpu) -> None:
        self.increment_register(cpu, cpu.x, -1)


class Dey(IncrementInstruction):
    def execute(self, cpu: Cpu) -> None:
        self.increment_register(cpu, cpu.y, -1)
