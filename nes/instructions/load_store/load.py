from nes.instructions import Instruction


class LoadInstruction(Instruction):
    register = None

    def execute(self, processor):
        reg = processor.registers[self.register]

        reg.value = self.read_source(processor)
        processor.p.z.update(reg.value)
        processor.p.n.update(reg.value)
