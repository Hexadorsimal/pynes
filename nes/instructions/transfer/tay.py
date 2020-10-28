from nes.instructions import Instruction


class Tay(Instruction):
    def execute(self):
        a = self.get('a')

        return {
            'y': a,
            'z': a == 0,
            'n': a & 0x80,
        }
