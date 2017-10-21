class Address:
    def evaluate(self, cpu):
        raise NotImplementedError


class PagedAddress(Address):
    def __init__(self, page, reg_lo):
        self.page = page
        self.reg_lo = reg_lo

    def evaluate(self, cpu):
        reg_lo = cpu.registers[self.reg_lo]
        return (self.page << 8) | reg_lo.contents


class ZeroPageAddress(PagedAddress):
    def __init__(self, reg_lo):
        super().__init__(0x00, reg_lo)


class StackAddress(PagedAddress):
    def __init__(self, reg_lo):
        super().__init__(0x01, reg_lo)


class FullAddress(Address):
    def __init__(self, reg_hi, reg_lo):
        self.reg_hi = reg_hi
        self.reg_lo = reg_lo

    def evaluate(self, cpu):
        reg_hi = cpu.registers[self.reg_hi]
        reg_lo = cpu.registers[self.reg_lo]
        return (reg_hi.contents << 8) | reg_lo.contents


class VectorAddress(Address):
    def __init__(self, vector, offset):
        self.vector = vector
        self.offset = offset

    def evaluate(self, cpu):
        vector = cpu.vectors[self.vector]
        return vector.address + self.offset
