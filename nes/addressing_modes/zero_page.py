from .addressing_mode import AddressingMode


class ZeroPageAddressingMode(AddressingMode):
    def read_parameter(self, processor):
        return processor.read(processor.pc.value + 1)
