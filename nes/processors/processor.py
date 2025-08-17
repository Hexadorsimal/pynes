class Processor:
    def __init__(self):
        self.clock = 0

    def power_on(self) -> None:
        self.clock = 0

    def power_off(self) -> None:
        pass

    def tick(self) -> None:
        self.clock += 1
