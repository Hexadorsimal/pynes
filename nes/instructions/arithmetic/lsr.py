from ..instruction import Instruction


class Lsr(Instruction):
    def execute(self):
        addr = self.addressing_mode.calculate_address()

        value = self.read(addr)
        value >>= 1

        return {
            'z': value == 0,
            'n': value & 0x80 != 0,
            'c': value & 0x01 != 0,
            'write': value,
        }
