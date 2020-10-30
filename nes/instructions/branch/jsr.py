from nes.instructions import Instruction


class Jsr(Instruction):
    def execute(self, processor):
        addr = self.parameter
        pc = processor.pc

        pc.value -= 1
        processor.push(pc.hi)
        processor.push(pc.lo)
        pc.value = addr
