from nes.bus import BusDevice


class Memory(BusDevice):
    def __init__(self, size):
        super().__init__('memory')
        self.size = size
