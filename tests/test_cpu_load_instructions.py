import unittest
from nes.cpu import Cpu
from nes.memory import Ram


class CpuLoadInstructionsTestCase(unittest.TestCase):
    def setUp(self):
        ram = Ram(256)
        self.cpu = Cpu(ram)
        ram.write(0x0000, 0xff)

    def test_lda(self):
        self.cpu.lda(0x0000)
        self.assertEqual(self.cpu.a, 0xff)

    def test_ldx(self):
        self.cpu.ldx(0x0000)
        self.assertEqual(self.cpu.x, 0xff)

    def test_ldy(self):
        self.cpu.ldy(0x0000)
        self.assertEqual(self.cpu.y, 0xff)


if __name__ == '__main__':
    unittest.main()
