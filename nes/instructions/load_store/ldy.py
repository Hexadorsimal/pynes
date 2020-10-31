from nes.instructions import Instruction


class Ldy(Instruction):
    def execute(self, processor):
        y = processor.y

        y.value = self.read_source(processor)
        processor.p.z.update(y.value)
        processor.p.n.update(y.value)
