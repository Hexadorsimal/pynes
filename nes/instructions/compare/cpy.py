from ..instruction import Instruction


class Cpy(Instruction):
    def execute(self, processor):
        y = processor.y.value
        mem = self.read_source(processor)

        diff = y - mem

        processor.p.z.update(diff)
        processor.p.n.update(diff)
        processor.p.c.update(y >= mem)
