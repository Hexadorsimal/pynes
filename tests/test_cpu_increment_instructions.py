import unittest
from nes.processors.cpu import Cpu
from nes.memory import Ram


class CpuIncrementInstructionsTestCase(unittest.TestCase):
    def setUp(self):
        self.ram = Ram(256)
        self.cpu = Cpu(self.ram)

    def test_inc(self):
        self.ram.write(0x0000, 0x00)
        self.cpu.inc(0x0000)
        self.assertEqual(self.ram.read(0x0000), 0x01)
        self.assertEqual(self.cpu.z, 0)
        self.assertEqual(self.cpu.n, 0)

    def test_inx(self):
        self.cpu.x = 0x00
        self.cpu.inx(None)
        self.assertEqual(self.cpu.x, 0x01)
        self.assertEqual(self.cpu.z, 0)
        self.assertEqual(self.cpu.n, 0)

    def test_iny(self):
        self.cpu.y = 0x00
        self.cpu.iny(None)
        self.assertEqual(self.cpu.y, 0x01)
        self.assertEqual(self.cpu.z, 0)
        self.assertEqual(self.cpu.n, 0)


if __name__ == '__main__':
    unittest.main()
