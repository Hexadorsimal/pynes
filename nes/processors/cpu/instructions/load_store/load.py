from nes.processors.registers import Register
from ..instruction import Instruction
from ... import Cpu


class LoadInstruction(Instruction):
    def load_register(self, cpu: Cpu, reg: Register) -> None:
        reg.value = self.read_source(cpu)
        cpu.p.z.update(reg.value)
        cpu.p.n.update(reg.value)


class Lda(LoadInstruction):
    def execute(self, cpu: Cpu) -> None:
        self.load_register(cpu, cpu.a)


class Ldx(LoadInstruction):
    def execute(self, cpu: Cpu) -> None:
        self.load_register(cpu, cpu.x)


class Ldy(LoadInstruction):
    def execute(self, cpu: Cpu) -> None:
        self.load_register(cpu, cpu.y)
