from .addressing_mode import AddressingMode


class ImmediateAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 2
