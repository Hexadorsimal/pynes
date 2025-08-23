from nes.processors.cpu import Cpu, Instruction


class Sec(Instruction):
    def execute(self, cpu: Cpu) -> None:
        cpu.p.c = True


class Sed(Instruction):
    def execute(self, cpu: Cpu) -> None:
        cpu.p.d = True


class Sei(Instruction):
    def execute(self, cpu: Cpu) -> None:
        cpu.p.i = True
