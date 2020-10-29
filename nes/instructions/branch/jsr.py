from nes.instructions import Instruction


class Jsr(Instruction):
    def execute(self, processor):
        addr = self.parameter
        pc = processor.registers['pc']

        processor.push16(pc - 1)
        pc.value = addr
