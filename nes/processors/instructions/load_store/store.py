from nes.processors.registers import Register
from nes.processors.cpu.instruction import Instruction
from nes.processors.cpu import Cpu


class StoreInstruction(Instruction):
    def store_register(self, cpu: Cpu, reg: Register) -> None:
        self.write_result(cpu, reg.value)


class Sta(StoreInstruction):
    def execute(self, cpu: Cpu) -> None:
        self.store_register(cpu, cpu.a)


class Stx(StoreInstruction):
    def execute(self, cpu: Cpu) -> None:
        self.store_register(cpu, cpu.x)


class Sty(StoreInstruction):
    def execute(self, cpu: Cpu) -> None:
        self.store_register(cpu, cpu.y)
