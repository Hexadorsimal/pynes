from .addressing_mode import AddressingMode


class AbsoluteAddressingMode(AddressingMode):
    def read_parameter(self, processor):
        return processor.read16(processor.registers['pc'] + 1)
