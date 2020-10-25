from .addressing_mode import AddressingMode


class ImmediateAddressingMode(AddressingMode):
    def calculate_address(self, processor):
        return processor.registers['pc'] + 1
