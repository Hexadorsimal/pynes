class AddressingMode:
    @property
    def instruction_size(self) -> int:
        raise NotImplementedError

    @property
    def parameter_size(self) -> int:
        return self.instruction_size - 1

    @staticmethod
    def pages_differ(a, b):
        return a & 0xFF00 != b & 0xFF00
