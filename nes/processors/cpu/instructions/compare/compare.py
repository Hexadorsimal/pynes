from ..instruction import Instruction


class CompareInstruction(Instruction):
    register = None

    def execute(self, processor):
        reg = processor.registers[self.register].value
        mem = self.read_source(processor)

        diff = reg - mem

        processor.p.z.update(diff)
        processor.p.n.update(diff)
        processor.p.c.update(reg >= mem)
