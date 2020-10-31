from ..instruction import Instruction


class Asl(Instruction):
    def execute(self, processor):
        value = self.read_source(processor)

        processor.p.c.update(value & 0x80)

        value = (value << 1) & 0xff

        processor.p.z.update(value)
        processor.p.n.update(value)

        self.write_result(processor, value)
