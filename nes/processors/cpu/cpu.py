from ..processor import Processor
from .decoder import Decoder
from .instruction_factory import InstructionFactory
from nes.processors.registers import GeneralPurposeRegister, ProgramCounter, StackPointer, ProcessorStatusRegister
from nes.bus import Bus


class Cpu(Processor):
    def __init__(self, bus: Bus, instruction_factory: InstructionFactory):
        super().__init__(bus)
        self.pc = ProgramCounter()
        self.a = GeneralPurposeRegister()
        self.x = GeneralPurposeRegister()
        self.y = GeneralPurposeRegister()
        self.p = ProcessorStatusRegister()
        self.s = StackPointer()

        self.decoder = Decoder()
        self.instruction_factory = instruction_factory
        self.cycles = 0

        self.nmi_vector = [0xff, 0xfa]
        self.reset_vector = [0xff, 0xfc]
        self.interrupt_vector = [0xff, 0xfe]

    def power_on(self) -> None:
        self.pc.hi.write(0xc0)
        self.pc.lo.write(0x00)
        self.s.write(0xfd)
        self.p.write(0x24)

    def nmi(self) -> None:
        opcode = self.decoder.decode(0x6c)
        jmpi = self.instruction_factory.create(opcode, self.nmi_vector)
        jmpi.execute(self)

    def reset(self) -> None:
        opcode = self.decoder.decode(0x6c)
        jmpi = self.instruction_factory.create(opcode, self.reset_vector)
        jmpi.execute(self)

    def irq(self) -> None:
        opcode = self.decoder.decode(0x6c)
        jmpi = self.instruction_factory.create(opcode, self.interrupt_vector)
        jmpi.execute(self)

    def tick(self) -> None:
        instruction = self.fetch_instruction()
        instruction.execute(self)
        super().tick()

    def fetch_instruction(self):
        byte = self.fetch_byte()
        opcode = self.decoder.decode(byte)
        params = []

        for i in range(opcode.param_count):
            params.append(self.fetch_byte())

        return self.instruction_factory.create(opcode, params)

    def fetch_byte(self) -> int:
        byte = self.bus.read(self.pc.read_address())
        self.pc += 1
        return byte

    def read(self, addr: int) -> int:
        return self.bus.read(addr)

    def write(self, addr: int, value: int) -> None:
        self.bus.write(addr, value)

    def push(self, value: int) -> None:
        self.bus.write(self.s.read_address(), value)
        self.s -= 1

    def pull(self):
        self.s += 1
        return self.bus.read(self.s.read_address())
