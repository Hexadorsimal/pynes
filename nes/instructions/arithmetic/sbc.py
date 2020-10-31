from ..instruction import Instruction


class Sbc(Instruction):
    def execute(self, processor):
        addr = self.parameter
        mem = processor.read(addr)
        acc = processor.a.value

        value = acc - mem
        if processor.p.c:
            value -= 1

        processor.p.n.update(value)
        processor.p.z.update(value)
        processor.p.v.update((acc ^ mem) & 0x80 and (acc ^ value) & 0x80)

        processor.p.c.update(value < 0x100)
        processor.a.value = value & 0xff
