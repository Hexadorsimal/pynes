from ..instruction import Instruction


class Bit(Instruction):
    def execute(self, processor):
        src = processor.read(self.parameter)

        processor.p.v.update(src)
        processor.p.z.update(processor.a.value & src)
        processor.p.n.update(src)
