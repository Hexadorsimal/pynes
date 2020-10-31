from nes.instructions import Instruction


class Lda(Instruction):
    def execute(self, processor):
        a = processor.a

        a.value = self.read_source(processor)
        processor.p.z.update(a.value)
        processor.p.n.update(a.value)
