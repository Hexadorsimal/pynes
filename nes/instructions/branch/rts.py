from nes.instructions import Instruction


class Rts(Instruction):
    def execute(self, processor):
        lo = processor.pull()
        hi = processor.pull()

        processor.pc.value = (hi << 8) | lo
        processor.pc.value += 1
