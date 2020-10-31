from ..instruction import Instruction


class TransferInstruction(Instruction):
    src = None
    dst = None
    update_flags = True

    def execute(self, processor):
        value = processor.registers[self.src].value
        processor.registers[self.dst].value = value

        if self.update_flags:
            processor.p.n.update(value)
            processor.p.z.update(value)
