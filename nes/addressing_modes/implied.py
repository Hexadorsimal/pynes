from .addressing_mode import AddressingMode


class ImpliedAddressingMode(AddressingMode):
    def read_parameter(self, processor):
        return None
