from nes.instructions import Instruction


class Ldy(Instruction):
    def execute(self):
        addr = self.addressing_mode.calculate_address()
        y = self.read(addr)

        return {
            'y': y,
            'z': y == 0,
            'n': y & 0x80 != 0,
        }
