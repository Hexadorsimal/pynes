from .addressing_mode import AddressingMode


class RelativeAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 2

    def calculate_address(self, processor, parameter):
        return processor.pc.value + parameter

    def read_source(self, processor, parameter):
        return self.calculate_address(processor, parameter)

    def write_result(self, processor, parameter, value):
        raise RuntimeError('This should never be called')
