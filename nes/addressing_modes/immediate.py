from .addressing_mode import AddressingMode


class ImmediateAddressingMode(AddressingMode):
    def read_parameters(self, processor):
        return processor.pc.value + 1
