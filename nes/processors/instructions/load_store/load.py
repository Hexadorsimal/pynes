from nes.processors.registers import Register
from nes.processors.cpu.instruction import Instruction
from nes.processors.cpu import Cpu


class LoadInstruction(Instruction):
    def load_register(self, cpu: Cpu, reg: Register) -> None:
        value = self.reader.read_parameter(cpu, self)
        reg.write(value)
        cpu.p.update_zero_flag(value)
        cpu.p.update_negative_flag(value)


class Lda(LoadInstruction):
    def execute(self, cpu: Cpu) -> None:
        self.load_register(cpu, cpu.a)


class Ldx(LoadInstruction):
    def execute(self, cpu: Cpu) -> None:
        self.load_register(cpu, cpu.x)


class Ldy(LoadInstruction):
    def execute(self, cpu: Cpu) -> None:
        self.load_register(cpu, cpu.y)
