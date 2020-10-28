from .addressing_mode import AddressingMode


class IndirectAddressingMode(AddressingMode):
    def calculate_address(self, processor):
        return processor.read16_bug(processor.read16(processor.registers['pc'] + 1))
