from nes.bus import BusDevice


class Memory(BusDevice):
    def __init__(self, size):
        self.size = size
