from ..instruction import Instruction
from nes.addressing_modes.accumulator import AccumulatorAddressingMode


class Rol(Instruction):
    def execute(self, processor):
        if isinstance(self.addressing_mode, AccumulatorAddressingMode):
            addr = None
            value = processor.a.value
        else:
            addr = self.parameter
            value = processor.read(addr)

        value = value << 1
        if processor.p.c:
            value |= 0x01

        processor.p.c.update(value > 0xff)
        value &= 0xff

        processor.p.z.update(value)
        processor.p.n.update(value)

        if isinstance(self.addressing_mode, AccumulatorAddressingMode):
            processor.a.value = value
        else:
            processor.write(addr, value)
