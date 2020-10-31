from ..instruction import Instruction


class Cpx(Instruction):
    def execute(self, processor):
        x = processor.x.value
        mem = self.read_source(processor)

        diff = x - mem

        processor.p.z.update(diff)
        processor.p.n.update(diff)
        processor.p.c.update(x >= mem)
