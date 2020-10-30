from nes.instructions import Instruction


class Lda(Instruction):
    def execute(self, processor):
        a = processor.a
        z = processor.p.z
        n = processor.p.n

        a.value = self.parameter
        z.update(a.value)
        n.update(a.value)
