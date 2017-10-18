import yaml
from cpu.processor import Processor
from cpu.register import Register
from cpu.flag_register import FlagRegister, Flag


class CpuImporter:
    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'rt') as stream:
            yaml_data = yaml.load(stream)
            registers = cls.import_registers(yaml_data['registers'])
            return Processor(registers)

    @classmethod
    def import_registers(cls, registers_dict):
        registers = []

        for register_dict in registers_dict:
            if 'flags' in register_dict:
                flags = cls.import_flags(register_dict)
                register = FlagRegister(name=register_dict.get('name'),
                                        description=register_dict.get('description'),
                                        flags=flags)
            else:
                register = Register(name=register_dict.get('name'),
                                    description=register_dict.get('description'))
            registers.append(register)
        return registers

    @staticmethod
    def import_flags(register_dict):
        flags = []

        if 'flags' in register_dict:
            for flag_dict in register_dict.get('flags'):
                flag = Flag(letter=flag_dict.get('letter'),
                            name=flag_dict.get('name'),
                            description=flag_dict.get('description'),
                            mask=flag_dict.get('mask'))
                flags.append(flag)
        return flags
