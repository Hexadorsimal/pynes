from nes.instructions import Instruction


class Rti(Instruction):
    def execute(self):
        status = self.processor.pull()
        addr = self.processor.pull16()

        return {
            'p': status,
            'pc': addr,
        }
