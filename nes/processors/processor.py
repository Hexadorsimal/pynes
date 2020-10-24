class Processor:
    def __init__(self, bus):
        self.bus = bus

    def power_on(self):
        raise NotImplementedError

    def step(self):
        raise NotImplementedError
