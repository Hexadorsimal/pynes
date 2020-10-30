from .addressing_mode import AddressingMode


class IndirectAddressingMode(AddressingMode):
    def read_parameter(self, processor):
        return processor.read16_bug(processor.read16(processor.pc.value + 1))
