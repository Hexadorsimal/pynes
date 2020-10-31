from .addressing_mode import AddressingMode


class IndexedIndirectAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 2
