from .register import Register


class Flag:
    def __init__(self, letter, name, description, mask):
        self.letter = letter
        self.name = name
        self.mask = mask
        self.description = description
        self.value = 0

    def set(self):
        self.value = 1

    def clear(self):
        self.value = 0

    def is_set(self):
        return self.value == 1


class FlagRegister(Register):
    def __init__(self, name, description, flags):
        super().__init__(name, description)

        self.flags = {}
        for flag in flags:
            self.flags[flag.letter] = flag

    def __repr__(self):
        flag_string = ""
        for (letter, flag) in self.flags.items():
            if flag.is_set():
                flag_string += flag.letter
            else:
                flag_string += '-'

        return "{name}:{flags}".format(name=self.name, flags=flag_string)

    @property
    def contents(self):
        val = 0
        for (letter, flag) in self.flags.items():
            if flag.set:
                val |= flag.mask
        return val
