from nes.bus import Bus


class Processor:
    def __init__(self, bus: Bus):
        self.bus = bus
        self.clock = 0

    def power_on(self) -> None:
        self.clock = 0

    def power_off(self) -> None:
        pass

    def tick(self) -> None:
        self.clock += 1
