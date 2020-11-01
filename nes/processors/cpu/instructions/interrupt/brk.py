from ..instruction import Instruction


class Brk(Instruction):
    def execute(self, processor):
        processor.push(processor.pc.hi)
        processor.push(processor.pc.lo)

        processor.p.b.set()
        processor.push(processor.p.value)

        processor.p.i.set()

        lo = processor.read(processor.interrupt_vector)
        hi = processor.read(processor.interrupt_vector + 1)
        processor.pc.value = (hi << 8) | lo
