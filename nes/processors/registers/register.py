class Register:
    def read(self):
        raise NotImplementedError()

    def write(self, value):
        raise NotImplementedError()
