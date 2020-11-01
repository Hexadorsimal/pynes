from .decoder import Decoder
from ..processor import Processor
from .registers import GeneralPurposeRegister, ProgramCounter, StackPointer, FlagRegister
from .registers.flags import Flag, NegativeFlag, ZeroFlag, OverflowFlag, CarryFlag
from .instructions import InstructionFactory


class Cpu(Processor):
    def __init__(self, bus=None):
        super().__init__(bus)
        self.registers = {
            'pc': ProgramCounter(),
            'a': GeneralPurposeRegister(),
            'x': GeneralPurposeRegister(),
            'y': GeneralPurposeRegister(),
            'p': FlagRegister({
                'n': NegativeFlag(mask=0x80),
                'v': OverflowFlag(mask=0x40),
                'x': Flag(mask=0x20),
                'b': Flag(mask=0x10),
                'd': Flag(mask=0x08),
                'i': Flag(mask=0x04),
                'z': ZeroFlag(mask=0x02),
                'c': CarryFlag(mask=0x01),
            }),
            's': StackPointer(),
        }

        self.decoder = Decoder()
        self.cycles = 0

        self.nmi_vector = 0xfffa
        self.reset_vector = 0xfffc
        self.interrupt_vector = 0xfffe

    def __repr__(self):
        return 'RICOH 2A03'

    @property
    def pc(self):
        return self.registers['pc']

    @property
    def a(self):
        return self.registers['a']

    @property
    def x(self):
        return self.registers['x']

    @property
    def y(self):
        return self.registers['y']

    @property
    def p(self):
        return self.registers['p']

    @property
    def s(self):
        return self.registers['s']

    def power_on(self):
        self.pc.value = 0xC000
        self.s.value = 0xFD
        self.p.value = 0x24

    def nmi(self):
        jmpi = InstructionFactory.create('jmp', 'indirect', self.nmi_vector)
        jmpi.execute(self)

    def reset(self):
        jmpi = InstructionFactory.create('jmp', 'indirect', self.reset_vector)
        jmpi.execute(self)

    def irq(self):
        jmpi = InstructionFactory.create('jmp', 'indirect', self.interrupt_vector)
        jmpi.execute(self)

    def tick(self):
        opcode = self.fetch()
        instruction = self.decode(opcode)
        self.pc.value += instruction.size
        self.execute(instruction)
        super().tick()

    def fetch(self):
        return self.bus.read(self.pc.value)

    def decode(self, opcode):
        info = self.decoder.decode(opcode)
        instruction = InstructionFactory.create(self,
                                                info['name'],
                                                info['addressing_mode'],
                                                info['cycles'],
                                                info['page_cycles'])
        return instruction

    def execute(self, instruction):
        instruction.execute(self)
        self.cycles += instruction.cycles

    def read(self, addr):
        return self.bus.read(addr)

    def write(self, addr, value):
        return self.bus.write(addr, value)

    def push(self, value):
        self.bus.write(self.s.pointer, value)
        self.s.value -= 1

    def pull(self):
        self.s.value += 1
        return self.bus.read(self.s.pointer)
