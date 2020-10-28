from nes.instructions import Instruction


class Cld(Instruction):
    def execute(self):
        return {
            'd': False
        }
