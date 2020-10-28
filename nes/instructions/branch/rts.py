from nes.instructions import Instruction


class Rts(Instruction):
    def execute(self):
        addr = self.processor.pull16()

        return {
            'pc': addr + 1,
        }
