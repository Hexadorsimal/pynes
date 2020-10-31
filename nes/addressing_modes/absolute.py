from .addressing_mode import AddressingMode


class AbsoluteAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 3

    def calculate_address(self, processor, parameter):
        return parameter
