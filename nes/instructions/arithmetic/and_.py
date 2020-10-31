from ..instruction import Instruction


class And(Instruction):
    def execute(self, processor):
        a = processor.a
        mem = self.read_source(processor)

        a.value &= mem
        processor.p.z.update(a.value)
        processor.p.n.update(a.value)
