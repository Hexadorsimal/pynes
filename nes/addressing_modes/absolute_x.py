from .addressing_mode import AddressingMode


class AbsoluteXAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 3
