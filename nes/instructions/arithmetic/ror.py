from ..instruction import Instruction
from nes.addressing_modes.accumulator import AccumulatorAddressingMode


class Ror(Instruction):
    def execute(self, processor):
        if isinstance(self.addressing_mode, AccumulatorAddressingMode):
            addr = None
            value = processor.a.value
        else:
            addr = self.parameter
            value = processor.read(addr)

        if processor.p.c:
            value |= 0x100
        processor.p.c.update(value & 0x01)

        value >>= 1

        processor.p.z.update(value)
        processor.p.n.update(value)

        if isinstance(self.addressing_mode, AccumulatorAddressingMode):
            processor.a.value = value
        else:
            processor.write(addr, value)

