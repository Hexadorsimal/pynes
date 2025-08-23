from nes.processors.cpu.instruction import Instruction
from nes.processors.cpu import Cpu


class Adc(Instruction):
    def execute(self, cpu: Cpu):
        acc = cpu.a
        mem = self.read_source(cpu)

        value = mem + acc
        if cpu.p.c:
            value += 1

        cpu.p.z.update(value)
        cpu.p.n.update(value)
        cpu.p.v.update(not ((acc ^ mem) & 0x80) and (acc ^ value) & 0x80)
