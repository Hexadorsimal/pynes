from ..instruction import Instruction


class Cmp(Instruction):
    def execute(self, processor):
        a = processor.a.value
        mem = self.read_source(processor)

        diff = a - mem

        processor.p.z.update(diff)
        processor.p.n.update(diff)
        processor.p.c.update(a >= mem)
