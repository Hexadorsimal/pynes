from .addressing_mode import AddressingMode


class AbsoluteYAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 3
