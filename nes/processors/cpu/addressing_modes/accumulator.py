from .addressing_mode import AddressingMode


class AccumulatorAddressingMode(AddressingMode):
    def calculate_address(self, processor):
        return processor.registers['a']
