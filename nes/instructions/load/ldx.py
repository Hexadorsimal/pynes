from nes.instructions import Instruction


class Ldx(Instruction):
    def execute(self):
        addr = self.addressing_mode.calculate_address()
        x = self.read(addr)

        return {
            'x': x,
            'z': x == 0,
            'n': x & 0x80 != 0,
        }
