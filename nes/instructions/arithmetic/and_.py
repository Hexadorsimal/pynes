from ..instruction import Instruction


class And(Instruction):
    def execute(self, processor):
        a = processor.a
        addr = self.parameter
        mem = processor.read(addr)

        a.value &= mem
        processor.p.z.update(a.value)
        processor.p.n.update(a.value)
