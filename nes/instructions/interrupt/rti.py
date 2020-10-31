from nes.instructions import Instruction


class Rti(Instruction):
    def execute(self, processor):
        processor.p.value = processor.pull()

        lo = processor.pull()
        hi = processor.pull()

        processor.pc.value = (hi >> 8) | lo
