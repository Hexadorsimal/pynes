from ..instruction import Instruction


class Sbc(Instruction):
    def execute(self, processor):
        acc = processor.a.value
        mem = self.read_source(processor)

        value = acc - mem
        if processor.p.c:
            value -= 1

        processor.p.n.update(value)
        processor.p.z.update(value)
        processor.p.v.update((acc ^ mem) & 0x80 and (acc ^ value) & 0x80)

        processor.p.c.update(value < 0x100)
        processor.a.value = value & 0xff
