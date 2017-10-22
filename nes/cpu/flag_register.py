from .flag import Flag
from .register import Register


class FlagRegister(Register):
    def __init__(self, name, description, flags):
        super().__init__(name, description)

        self.flags = {}
        for flag_dict in flags:
            flag = Flag(**flag_dict)
            self.flags[flag.letter] = flag

    def is_flag_set(self, letter):
        flag = self.flags[letter]
        if self.contents & flag.mask:
            return True
        else:
            return False

    def set_flag(self, letter):
        flag = self.flags[letter]
        self.contents |= flag.mask

    def clear_flag(self, letter):
        flag = self.flags[letter]
        self.contents &= ~flag.mask
