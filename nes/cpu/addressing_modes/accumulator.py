from .addressing_mode import AddressingMode


class AccumulatorAddressing(AddressingMode):
    @property
    def size(self):
        return 1
