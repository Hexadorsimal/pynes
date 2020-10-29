from .addressing_mode import AddressingMode


class AccumulatorAddressingMode(AddressingMode):
    def read_parameters(self, processor):
        return processor.a.value
