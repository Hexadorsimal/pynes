from nes.instructions import Instruction


class Ldy(Instruction):
    def execute(self, processor):
        y = processor.y
        z = processor.p.z
        n = processor.p.n

        y.value = self.parameter
        z.update(y.value)
        n.update(y.value)
