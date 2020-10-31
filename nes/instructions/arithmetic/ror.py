from ..instruction import Instruction


class Ror(Instruction):
    def execute(self, processor):
        value = self.read_source(processor)

        if processor.p.c:
            value |= 0x100
        processor.p.c.update(value & 0x01)

        value >>= 1

        processor.p.z.update(value)
        processor.p.n.update(value)

        self.write_result(processor, value)
