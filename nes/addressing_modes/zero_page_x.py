from .addressing_mode import AddressingMode


class ZeroPageXAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 3
