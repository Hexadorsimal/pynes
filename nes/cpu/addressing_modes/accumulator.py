from .addressing_mode import AddressingMode


class AccumulatorAddressing(AddressingMode):
    def __init__(self):
        super().__init__()

    @property
    def size(self):
        return 1
