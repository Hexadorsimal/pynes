from .addressing_mode import AddressingMode


class IndirectIndexedAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 2
