from .decoder import Decoder
from ..processor import Processor
from .instructions import InstructionFactory
from nes.processors.registers import GeneralPurposeRegister, ProgramCounter, StackPointer, ProcessorStatusRegister
from nes.bus import Bus


class Cpu(Processor):
    def __init__(self, bus: Bus = None):
        super().__init__()
        self.pc = ProgramCounter()
        self.a = GeneralPurposeRegister()
        self.x = GeneralPurposeRegister()
        self.y = GeneralPurposeRegister()
        self.p = ProcessorStatusRegister()
        self.s = StackPointer()

        self.bus = bus

        self.decoder = Decoder()
        self.cycles = 0

        self.nmi_vector = 0xfffa
        self.reset_vector = 0xfffc
        self.interrupt_vector = 0xfffe

    def __repr__(self) -> str:
        return 'RICOH 2A03'

    def power_on(self) -> None:
        self.pc.value = 0xC000
        self.s.value = 0xFD
        self.p.value = 0x24

    def nmi(self) -> None:
        jmpi = InstructionFactory.create('jmp', 'indirect', self.nmi_vector)
        jmpi.execute(self)

    def reset(self) -> None:
        jmpi = InstructionFactory.create('jmp', 'indirect', self.reset_vector)
        jmpi.execute(self)

    def irq(self) -> None:
        jmpi = InstructionFactory.create('jmp', 'indirect', self.interrupt_vector)
        jmpi.execute(self)

    def tick(self) -> None:
        opcode = self.fetch()
        instruction = self.decode(opcode)

        print(f'{self.pc.value:X}  {opcode:X} {instruction}')

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
