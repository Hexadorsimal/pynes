from .addressing_mode import AddressingMode


class ZeroPageXAddressingMode(AddressingMode):
    def read_parameters(self, processor):
        return (processor.read(processor.pc.value + 1) + processor.x.value) & 0xff
