from .addressing_mode import AddressingMode


class RelativeAddressingMode(AddressingMode):
    def read_parameter(self, processor):
        return processor.read(processor.pc.value + 1)
