import yaml
from .flag_register import Flag, FlagRegister
from .register import Register


class Processor:
    def __init__(self, registers):
        self.registers = {}
        for register in registers:
            self.registers[register.name] = register

        self.cycle_queue = []

    @classmethod
    def load(cls, filename):
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

    def step(self):
        if self.cycle_queue:
            cycle = self.cycle_queue.pop(0)
            for operation in cycle:
                operation.execute()
