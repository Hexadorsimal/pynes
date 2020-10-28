from nes.instructions import Instruction


class Dec(Instruction):
    def execute(self):
        addr = self.addressing_mode.calculate_address()
        value = self.read(addr) - 1

        return {
            'write': value,
            'z': value == 0,
            'n': value & 0x80 != 0,
        }
