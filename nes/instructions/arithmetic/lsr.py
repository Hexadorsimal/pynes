from ..instruction import Instruction
from nes.addressing_modes.accumulator import AccumulatorAddressingMode


class Lsr(Instruction):
    def execute(self, processor):
        if isinstance(self.addressing_mode, AccumulatorAddressingMode):
            addr = None
            value = processor.a.value
        else:
            addr = self.parameter
            value = processor.read(addr)

        processor.p.c.update(value & 0x01)

        value = (value >> 1) & 0xff

        processor.p.z.update(value)
        processor.p.n.update(value)

        if isinstance(self.addressing_mode, AccumulatorAddressingMode):
            processor.a.value = value
        else:
            processor.write(addr, value)
