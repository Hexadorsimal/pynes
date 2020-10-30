from .addressing_mode import AddressingMode


class AbsoluteAddressingMode(AddressingMode):
    def read_parameter(self, processor):
        lo = processor.read(processor.pc + 1)
        hi = processor.read(processor.pc + 2)
        return (hi << 8) | lo
