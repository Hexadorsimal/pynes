from .addressing_mode import AddressingMode


class ImmediateAddressingMode(AddressingMode):
    def read_parameter(self, processor):
        return processor.read(processor.pc + 1)
