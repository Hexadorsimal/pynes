from nes.instructions import Instruction


class Pla(Instruction):
    def execute(self):
        stack = self.processor.pull()

        return {
            'a': stack,
            'z': stack == 0,
            'n': stack & 0x80 != 0,
        }
