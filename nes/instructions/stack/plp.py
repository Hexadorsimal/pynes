from nes.instructions import Instruction


class Plp(Instruction):
    def execute(self):
        stack = self.processor.pull()

        return {
            'p': stack,
        }
