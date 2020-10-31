from ..instruction import Instruction


class Bit(Instruction):
    def execute(self, processor):
        value = self.read_source(processor)

        processor.p.v.update(value & 0x40)
        processor.p.z.update(processor.a.value & value)
        processor.p.n.update(value)
