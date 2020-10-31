from .addressing_mode import AddressingMode


class IndirectAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 3
