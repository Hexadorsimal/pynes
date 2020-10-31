from .addressing_mode import AddressingMode


class ImpliedAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 1
