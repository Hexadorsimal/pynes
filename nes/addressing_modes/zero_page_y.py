from .addressing_mode import AddressingMode


class ZeroPageYAddressingMode(AddressingMode):
    def read_parameters(self, processor):
        return (processor.read(processor.pc.value + 1) + processor.y.value) & 0xff
