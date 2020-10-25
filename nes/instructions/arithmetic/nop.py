from nes.instructions import Instruction


class Nop(Instruction):
    def execute(self):
        return {}
