from nes.processors.cpu import Cpu, Instruction


class Clc(Instruction):
    def execute(self, cpu: Cpu) -> None:
        cpu.p.c = False


class Cld(Instruction):
    def execute(self, cpu: Cpu) -> None:
        cpu.p.d = False


class Cli(Instruction):
    def execute(self, cpu: Cpu) -> None:
        cpu.p.i = False


class Clv(Instruction):
    def execute(self, cpu: Cpu) -> None:
        cpu.p.v = False
