from .register import Register


class Counter(Register):
    def __init__(self, *args, **kwargs):
        super(Counter, self).__init__(*args, **kwargs)
        self.data = 0

    def __repr__(self):
        return "<Counter {name}: {data}>".format(name=self.name, data=self.data)

    @property
    def value(self):
        return self.data

    def inc(self):
        self.data += 1
        if self.data >= 0x100:
            self.data -= 0x100
            return 1
        else:
            return 0

    def dec(self):
        self.data -= 1
