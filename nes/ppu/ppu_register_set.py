import yaml
from ..memory import MemoryMap, AddressRange
from nes.cpu.registers import Register


class PpuRegisterSet(MemoryMap):
    @classmethod
    def create(cls, filename):
        base_address = 0x2000
        ppu_register_set = PpuRegisterSet(8)

        with open(filename, 'rt') as stream:
            yaml_data = yaml.load(stream)
            registers = cls.load_registers(yaml_data['registers'])

            for address, register in registers.items():
                reg_local_addr = address - base_address
                ppu_register_set.add_memory(AddressRange(reg_local_addr, 1), register)

        return ppu_register_set

    @classmethod
    def load_registers(cls, registers_dict):
        registers = {}
        for register_dict in registers_dict:
            register = Register(name=register_dict.get('name'),
                                description=register_dict.get('description'))
            address = register_dict.get('address')
            registers[address] = register
        return registers
