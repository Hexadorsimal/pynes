from .addressing_mode import AddressingMode


class ImpliedAddressing(AddressingMode):
    @property
    def size(self):
        return 1
