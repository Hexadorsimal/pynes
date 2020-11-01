import unittest
from nes.processors.cpu import Cpu


class CpuSetInstructionsTestCase(unittest.TestCase):
    def setUp(self):
        self.cpu = Cpu()

    def test_sec(self):
        instruction = self.cpu.decode(opcode=0x38)
        self.cpu.execute(instruction)
        self.assertTrue(self.cpu.p.c)

    def test_sed(self):
        instruction = self.cpu.decode(opcode=0xF8)
        self.cpu.execute(instruction)
        self.assertTrue(self.cpu.p.d)

    def test_sei(self):
        instruction = self.cpu.decode(opcode=0x78)
        self.cpu.execute(instruction)
        self.assertTrue(self.cpu.p.i)


if __name__ == '__main__':
    unittest.main()
