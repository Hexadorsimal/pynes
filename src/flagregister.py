from .register import Register


class StatusFlag:
    def __init__(self, letter, name, mask, description):
        self.letter = letter
        self.name = name
        self.mask = mask
        self.description = description
        self.value = True

    def __repr__(self):
        if self.value:
            return self.letter
        else:
            return "-"


class FlagRegister(Register):
    def __init__(self, flags, *args, **kwargs):
        super(FlagRegister, self).__init__(*args, **kwargs)

        self.flags = {}
        for flag in flags:
            self.flags[flag.letter] = flag

    def __repr__(self):
        flag_string = ""
        for (letter, flag) in self.flags.items():
            flag_string += str(flag)

        return "<FlagRegister {name}:{flags}>".format(name=self.name, flags=flag_string)

