from ..instruction import Instruction


class Rol(Instruction):
    def execute(self, processor):
        value = self.read_source(processor)

        value = value << 1
        if processor.p.c:
            value |= 0x01

        processor.p.c.update(value > 0xff)
        value &= 0xff

        processor.p.z.update(value)
        processor.p.n.update(value)

        self.write_result(processor, value)
