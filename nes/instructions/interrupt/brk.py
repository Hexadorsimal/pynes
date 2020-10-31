from nes.instructions import Instruction


class Brk(Instruction):
    def execute(self, processor):
        processor.push(processor.pc.hi)
        processor.push(processor.pc.lo)

        processor.p.b.set()
        processor.push(processor.p.value)

        processor.p.i.set()

        lo = processor.read(0xfffe)
        hi = processor.read(0xffff)
        processor.pc.value = (hi << 8) | lo
