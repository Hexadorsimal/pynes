from nes.instructions import Instruction


class Tax(Instruction):
    def execute(self, processor):
        value = processor.a.value

        processor.x.value = value
        processor.p.n.update(value)
        processor.p.z.update(value)
