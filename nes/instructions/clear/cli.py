from nes.instructions import Instruction


class Cli(Instruction):
    def execute(self):
        return {
            'i': False
        }
