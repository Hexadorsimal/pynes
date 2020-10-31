from nes.bus import BusDevice


class Memory(BusDevice):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
