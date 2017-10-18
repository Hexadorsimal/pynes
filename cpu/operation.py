class Operation:
    def execute(self, processor):
        raise NotImplementedError


class SetFlagOperation(Operation):
    def __init__(self, flag):
        self.flag = flag

    def execute(self, processor):
        flag_register = processor.registers['P']
        flag_register.set_flag(self.flag)


class ClearFlagOperation(Operation):
    def __init__(self, flag):
        self.flag = flag

    def execute(self, processor):
        flag_register = processor.registers['P']
        flag_register.clear_flag(self.flag)


class MoveOperation(Operation):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def execute(self, processor):
        src_register = processor.registers[self.src]
        dst_register = processor.registers[self.dst]
        dst_register.contents = src_register.contents


class IncrementOperation(Operation):
    def __init__(self, register, overflow_register=None):
        self.register = register
        self.overflow_register = overflow_register

    def execute(self, processor):
        register = processor.registers[self.register]
        overflow = register.inc()
        if overflow:
            overflow_register = processor.registers[self.overflow_register]
            overflow_register.inc()


class DecrementOperation(Operation):
    def __init__(self, register):
        self.register = register

    def execute(self, processor):
        register = processor.registers[self.register]
        register.dec()


class ReadOperation(Operation):
    def __init__(self, addr_hi, addr_lo, dst):
        self.addr_hi = addr_hi
        self.addr_lo = addr_lo
        self.dst = dst

    def execute(self, processor):
        dst = processor.registers[self.dst]
        dst.contents = processor.read_memory(self.addr_hi, self.addr_lo)


class WriteOperation(Operation):
    def __init__(self, addr_hi, addr_lo, src):
        self.addr_hi = addr_hi
        self.addr_lo = addr_lo
        self.src = src

    def execute(self, processor):
        src = processor.registers[self.src]
        processor.write_memory(self.addr_hi, self.addr_lo, src.contents)


class BranchOperation(Operation):
    def __init__(self, flag, is_set):
        self.flag = flag
        self.is_set = is_set

    def execute(self, processor):
        flags_register = processor.registers['P']
        if flags_register.is_flag_set(self.flag) == self.is_set:
            offset = processor.registers['DL'].data
            processor.registers['PCL'].data += offset
            if processor.registers['PCL'] >= 0x100:
                processor.registers['PCL'].data -= 0x100
                processor.registers['PCH'].data += 0x100
