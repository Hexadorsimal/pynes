from nes.instructions import Instruction


class Txa(Instruction):
    def execute(self, processor):
        value = processor.x.value

        processor.a.value = value
        processor.p.n.update(value)
        processor.p.z.update(value)
