from .constant_register import ConstantRegister
from .flag_register import FlagRegister
from .register import Register


class RegisterFactory:
    @staticmethod
    def create_register(register_dict):
        if 'flags' in register_dict:
            return FlagRegister(**register_dict)
        elif 'value' in register_dict:
            return ConstantRegister(**register_dict)
        else:
            return Register(**register_dict)
