from nes.instructions import Instruction


class Sei(Instruction):
    def execute(self):
        return {
            'i': True,
        }
