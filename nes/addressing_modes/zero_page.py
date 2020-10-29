from .addressing_mode import AddressingMode


class ZeroPageAddressingMode(AddressingMode):
    def read_parameters(self, processor):
        return processor.read(processor.pc.value + 1)
