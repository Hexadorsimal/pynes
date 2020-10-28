from nes.instructions import Instruction


class Lda(Instruction):
    def execute(self):
        addr = self.addressing_mode.calculate_address()
        a = self.read(addr)

        return {
            'a': a,
            'z': a == 0,
            'n': a & 0x80 != 0,
        }
