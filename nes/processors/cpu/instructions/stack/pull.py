from ..instruction import Instruction


class PullInstruction(Instruction):
    dst_reg = None
    update_flags = True

    def execute(self, processor):
        value = processor.pull()
        processor.registers[self.dst_reg].value = value

        if self.update_flags:
            processor.p.z.update(value)
            processor.p.n.update(value)
