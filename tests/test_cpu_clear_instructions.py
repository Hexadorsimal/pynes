import unittest

from nes.bus import Bus
from nes.processors.cpu import Cpu
from nes.processors.cpu.instructions import InstructionFactory


class CpuClearInstructionsTestCase(unittest.TestCase):
    def setUp(self):
        self.cpu = Cpu(Bus())

    def test_clc(self):
        opcode = self.cpu.decoder.decode(opcode=0x18)
        instruction = InstructionFactory.create(opcode, [])
        instruction.execute(self.cpu)
        self.assertFalse(self.cpu.p.c)

    def test_cld(self):
        instruction = self.cpu.decode(opcode=0xD8)
        self.cpu.execute(instruction)
        self.assertFalse(self.cpu.p.d)

    def test_cli(self):
        instruction = self.cpu.decode(opcode=0x58)
        self.cpu.execute(instruction)
        self.assertFalse(self.cpu.p.i)

    def test_clv(self):
        instruction = self.cpu.decode(opcode=0xB8)
        self.cpu.execute(instruction)
        self.assertFalse(self.cpu.p.v)


if __name__ == '__main__':
    unittest.main()
