from nes.instructions import Instruction


class Inx(Instruction):
    def execute(self):
        x = self.get('x') + 1

        return {
            'x': x,
            'z': x == 0,
            'n': x & 0x80 != 0,
        }
