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

    def dec(self):
        self.data -= 1
