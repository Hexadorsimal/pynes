from .addressing_mode import AddressingMode


class ZeroPageXAddressingMode(AddressingMode):
    def calculate_address(self, processor):
        return (processor.bus.read(processor.registers['pc'] + 1) + processor.registers['x']) & 0xff
