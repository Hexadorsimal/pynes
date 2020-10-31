from nes.instructions import Instruction


class Jsr(Instruction):
    def execute(self, processor):
        subroutine_addr = self.read_source(processor)
        pc = processor.pc

        pc.value -= 1
        processor.push(pc.hi)
        processor.push(pc.lo)
        pc.value = subroutine_addr
