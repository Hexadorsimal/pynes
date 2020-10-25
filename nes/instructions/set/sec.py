from nes.instructions import Instruction


class Sec(Instruction):
    def execute(self):
        return {
            'c': True,
        }
