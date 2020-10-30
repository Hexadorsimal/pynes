from nes.instructions import Instruction


class Ldx(Instruction):
    def execute(self, processor):
        x = processor.x
        z = processor.p.z
        n = processor.p.n

        x.value = self.parameter
        z.update(x.value)
        n.update(x.value)
