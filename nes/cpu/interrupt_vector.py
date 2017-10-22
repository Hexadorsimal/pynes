class InterruptVector:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return hex(self.address)
