from ..instruction import Instruction


class Jsr(Instruction):
    def execute(self, processor):
        subroutine_addr = self.addressing_mode.calculate_address(processor, self.parameter)
        pc = processor.pc

        pc.value -= 1
        processor.push(pc.hi)
        processor.push(pc.lo)
        pc.value = subroutine_addr
