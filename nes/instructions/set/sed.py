from nes.instructions import Instruction


class Sed(Instruction):
    def execute(self):
        return {
            'd': True,
        }
