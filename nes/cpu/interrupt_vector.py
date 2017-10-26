class InterruptVector:
    def __init__(self, name, lo, hi):
        self.name = name
        self.lo = lo
        self.hi = hi

    def __repr__(self):
        return '({lo},{hi})'.format(lo=hex(self.lo), hi=hex(self.hi))
