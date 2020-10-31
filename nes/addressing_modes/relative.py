from .addressing_mode import AddressingMode


class RelativeAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 2
