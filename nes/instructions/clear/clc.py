from nes.instructions import Instruction


class Clc(Instruction):
    def execute(self):
        return {
            'c': False
        }
