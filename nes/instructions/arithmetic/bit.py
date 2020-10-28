from ..instruction import Instruction


class Bit(Instruction):
    def execute(self):
        addr = self.addressing_mode.calculate_address()
        value = self.read(addr)

        a = self.get('a')

        return {
            'v': (value >> 6) & 0x01,
            'z': value & a == 0,
            'n': value & 0x80 != 0,
        }
