from .addressing_mode import AddressingMode


class ZeroPageYAddressingMode(AddressingMode):
    def calculate_address(self, processor):
        return (processor.bus.read(processor.registers['pc'] + 1) + processor.registers['y']) & 0xff
