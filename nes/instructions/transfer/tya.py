from nes.instructions import Instruction


class Tya(Instruction):
    def execute(self, processor):
        value = processor.y.value

        processor.a.value = value
        processor.p.n.update(value)
        processor.p.z.update(value)
