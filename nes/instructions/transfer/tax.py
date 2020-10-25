from nes.instructions import Instruction


class Tax(Instruction):
    def execute(self):
        a = self.get('a')

        return {
            'x': a,
            'z': a == 0,
            'n': a & 0x80,
        }
