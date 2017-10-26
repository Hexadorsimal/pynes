from .microinstruction import Microinstruction


class SetFlag(Microinstruction):
    def __init__(self, flag):
        self.flag = flag

    def __repr__(self):
        return self.flag + ' <- 1'

    def execute(self, processor):
        flag_register = processor.registers['P']
        flag_register.set_flag(self.flag)


class ClearFlag(Microinstruction):
    def __init__(self, flag):
        self.flag = flag

    def __repr__(self):
        return self.flag + ' <- 0'

    def execute(self, processor):
        flag_register = processor.registers['P']
        flag_register.clear_flag(self.flag)


class Move(Microinstruction):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def __repr__(self):
        return self.dst + ' <- ' + self.src

    def execute(self, processor):
        src_register = processor.registers[self.src]
        dst_register = processor.registers[self.dst]
        dst_register.contents = src_register.contents


class AddressBusSelect(Microinstruction):
    def __init__(self, selection):
        self.selection = selection

    def __repr__(self):
        return 'AB_SEL <- ' + str(self.selection)

    def execute(self, cpu):
        if self.selection == 'PCX':
            addr_lo = cpu.registers['PCL'].contents
            addr_hi = cpu.registers['PCH'].contents
            addr = (addr_hi << 8) | addr_lo
        elif self.selection == 'ADX':
            addr_lo = cpu.registers['ADL'].contents
            addr_hi = cpu.registers['ADH'].contents
            addr = (addr_hi << 8) | addr_lo
        elif self.selection == 'BAX':
            addr_lo = cpu.registers['BAL'].contents
            addr_hi = cpu.registers['BAH'].contents
            addr = (addr_hi << 8) | addr_lo
        elif self.selection == 'AD_ZERO':
            addr_lo = cpu.registers['ADL'].contents
            addr_hi = 0x00
            addr = (addr_hi << 8) | addr_lo
        elif self.selection == 'BA_ZERO':
            addr_lo = cpu.registers['BAL'].contents
            addr_hi = 0x00
            addr = (addr_hi << 8) | addr_lo
        elif self.selection == 'STACK':
            addr_lo = cpu.registers['S'].contents
            addr_hi = 0x01
            addr = (addr_hi << 8) | addr_lo
        elif self.selection == 'NMI_LO':
            addr = cpu.vectors['NMI'].lo
        elif self.selection == 'NMI_HI':
            addr = cpu.vectors['NMI'].hi
        elif self.selection == 'RES_LO':
            addr = cpu.vectors['RESET'].lo
        elif self.selection == 'RES_HI':
            addr = cpu.vectors['RESET'].hi
        elif self.selection == 'IRQ_LO':
            addr = cpu.vectors['IRQ/BRK'].lo
        elif self.selection == 'IRQ_HI':
            addr = cpu.vectors['IRQ/BRK'].hi
        else:
            raise ValueError('Invalid Address Bus Selector: ' + self.selection)

        cpu.buses['AB'].put(addr)


class Read(Microinstruction):
    def __repr__(self):
        return 'R/W <- 1'

    def execute(self, cpu):
        cpu.buses['R/W'].put(1)


class Write(Microinstruction):
    def __repr__(self):
        return 'R/W <- 0'

    def execute(self, cpu):
        cpu.buses['R/W'].put(0)
        cpu.buses['DB'].put(cpu.registers['DL'].contents)


class Branch(Microinstruction):
    def __init__(self, flag, is_set):
        self.flag = flag
        self.is_set = is_set

    def __repr__(self):
        return 'Branch on {flag} = {value}'.format(flag=self.flag, value = self.is_set)

    def execute(self, processor):
        flags_register = processor.registers['P']
        if flags_register.is_flag_set(self.flag) == self.is_set:
            offset = processor.registers['DL'].data
            processor.registers['PCL'].data += offset
            if processor.registers['PCL'] >= 0x100:
                processor.registers['PCL'].data -= 0x100
                processor.registers['PCH'].data += 0x100
