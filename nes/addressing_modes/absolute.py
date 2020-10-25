from .addressing_mode import AddressingMode


class AbsoluteAddressingMode(AddressingMode):
    def calculate_address(self, processor):
        return processor.read16(processor.registers['pc'] + 1)
