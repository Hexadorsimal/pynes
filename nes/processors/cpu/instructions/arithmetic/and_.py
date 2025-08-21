from ..instruction import Instruction
from ... import Cpu


class And(Instruction):
    def execute(self, cpu: Cpu) -> None:
        a = cpu.a.read()
        mem = self.read_source(cpu)

        a.value &= mem
        cpu.p.z.update(a.value)
        cpu.p.n.update(a.value)
