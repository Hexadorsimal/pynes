from .addressing_mode import AddressingMode


class ImpliedAddressingMode(AddressingMode):
    def calculate_address(self, processor):
        return 0
