from .operation import Operation


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


class ReadOperation(Operation):
    def __init__(self, addr, dst):
        self.addr = addr
        self.dst = dst

    def execute(self, processor):
        dst = processor.registers[self.dst]
        addr = self.addr.evaluate(processor)
        dst.contents = processor.memory.read(addr)


class WriteOperation(Operation):
    def __init__(self, addr, src):
        self.addr = addr
        self.src = src

    def execute(self, processor):
        src = processor.registers[self.src]
        addr = self.addr.evaluate(processor)
        processor.memory.write(addr, src.contents)


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
