from nes.processors.cpu import Cpu


class AddressingMode:
    @property
    def instruction_size(self) -> int:
        raise NotImplementedError

    @property
    def parameter_size(self) -> int:
        return self.instruction_size - 1

    def calculate_address(self, cpu: Cpu, parameter):
        raise NotImplementedError

    def read_source(self, cpu: Cpu, parameter):
        addr = self.calculate_address(cpu, parameter)
        return cpu.read(addr)

    def write_result(self, cpu: Cpu, parameter, value) -> None:
        addr = self.calculate_address(cpu, parameter)
        cpu.write(addr, value)

    @staticmethod
    def pages_differ(a, b):
        return a & 0xFF00 != b & 0xFF00
