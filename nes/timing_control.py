class TimingControl:
    def __init__(self):
        self.cycle = 0

    def get(self):
        return self.cycle

    def inc(self):
        self.cycle += 1

    def reset(self):
        self.cycle = 0
