from .addressing_mode import AddressingMode


class AccumulatorAddressingMode(AddressingMode):
    @property
    def instruction_size(self):
        return 1

    def calculate_address(self, processor, parameter):
        raise RuntimeError('This should never be called')

    def read_source(self, processor, parameter):
        return processor.a.value

    def write_result(self, processor, parameter, value):
        processor.a.value = value
