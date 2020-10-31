from nes.instructions import Instruction


class Ldx(Instruction):
    def execute(self, processor):
        x = processor.x

        x.value = self.read_source(processor)
        processor.p.z.update(x.value)
        processor.p.n.update(x.value)
