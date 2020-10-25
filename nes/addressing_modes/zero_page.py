from .addressing_mode import AddressingMode


class ZeroPageAddressingMode(AddressingMode):
    def calculate_address(self, processor):
        return processor.bus.read(processor.registers['pc'] + 1)
