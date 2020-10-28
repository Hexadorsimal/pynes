from ..instruction import Instruction


class Rol(Instruction):
    def execute(self):
        addr = self.addressing_mode.calculate_address()
        a0 = self.read(addr)
        c0 = self.get('c')

        a = (a0 << 1) | c0

        return {
            'write': a,
            'c': (a >> 7) & 0x01,
            'z': a == 0,
            'n': a & 0x80 != 0,
        }
