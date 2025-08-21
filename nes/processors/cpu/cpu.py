from .decoder import Decoder
from nes.processors.cpu.addressing_modes import get_addressing_mode
from ..processor import Processor
from .instructions import Instruction
from nes.processors.registers import GeneralPurposeRegister, ProgramCounter, StackPointer, ProcessorStatusRegister
from nes.bus import Bus


class Cpu(Processor):
    def __init__(self, bus: Bus):
        super().__init__(bus)
        self.pc = ProgramCounter()
        self.a = GeneralPurposeRegister()
        self.x = GeneralPurposeRegister()
        self.y = GeneralPurposeRegister()
        self.p = ProcessorStatusRegister()
        self.s = StackPointer()

        self.decoder = Decoder()
        self.cycles = 0

        self.nmi_vector = 0xfffa
        self.reset_vector = 0xfffc
        self.interrupt_vector = 0xfffe

    def power_on(self) -> None:
        self.pc.value = 0xC000
        self.s.value = 0xFD
        self.p.value = 0x24

    def nmi(self) -> None:
        opcode = self.decoder.decode(108)
        jmpi = Instruction(opcode, bytes(self.nmi_vector))
        jmpi.execute(self)

    def reset(self) -> None:
        opcode = self.decoder.decode(108)
        jmpi = Instruction(opcode, bytes(self.reset_vector))
        jmpi.execute(self)

    def irq(self) -> None:
        opcode = self.decoder.decode(108)
        jmpi = Instruction(opcode, bytes(self.interrupt_vector))
        jmpi.execute(self)

    def tick(self) -> None:
        instruction = self.fetch_instruction()
        instruction.execute(self)
        super().tick()

    def fetch_instruction(self) -> Instruction:
        byte = self.fetch_byte()
        data = bytearray(byte)
        opcode = self.decoder.decode(byte)

        for i in range(opcode.addressing_mode.parameter_size):
            data.append(self.fetch_byte())

        return Instruction(opcode, bytes(data))

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
        self.s.value -= 1

    def pull(self):
        self.s.value += 1
        return self.bus.read(self.s.read_address())
