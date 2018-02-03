from .flag import Flag
from .register import Register


class FlagRegister(Register):
    def __init__(self, name, description, flags):
        super().__init__(name, description)

        self.flags = {}
        for flag_dict in flags:
            flag = Flag(**flag_dict)
            self.flags[flag.letter] = flag

    def __repr__(self):
        flag_string = ""
        for (name, flag) in self.flags.items():
            if self.is_flag_set(name):
                flag_string += flag.letter
            else:
                flag_string += '-'

        return '{name}:{hex}:{flags}'.format(name=self.name, hex=hex(self.contents), flags=flag_string)

    def is_flag_set(self, name):
        flag = self.flags[name]
        if self.contents & flag.mask:
            return True
        else:
            return False

    def set_flag_value(self, name, value):
        if value:
            self.set_flag(name)
        else:
            self.clear_flag(name)

    def get_flag_value(self, name):
        if self.is_flag_set(name):
            return 1
        else:
            return 0

    def set_flag(self, name):
        flag = self.flags[name]
        self.contents |= flag.mask

    def clear_flag(self, name):
        flag = self.flags[name]
        self.contents &= ~flag.mask
