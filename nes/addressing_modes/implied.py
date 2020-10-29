from .addressing_mode import AddressingMode


class ImpliedAddressingMode(AddressingMode):
    def read_parameters(self, processor):
        return 0
