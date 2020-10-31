from .addressing_mode import AddressingMode


class ZeroPageAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 2

    def calculate_address(self, processor, parameter):
        return parameter
