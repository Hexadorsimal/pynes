import unittest
from nes.cpu import Cpu
from nes.memory import Ram


class CpuDecrementInstructionsTestCase(unittest.TestCase):
    def setUp(self):
        self.ram = Ram(256)
        self.cpu = Cpu(self.ram)

    def test_dec(self):
        self.ram.write(0x0000, 0x01)
        self.cpu.dec(0x0000)
        self.assertEqual(self.ram.read(0x0000), 0x00)
        self.assertEqual(self.cpu.z, 1)
        self.assertEqual(self.cpu.n, 0)

    def test_dex(self):
        self.cpu.x = 0x01
        self.cpu.dex(None)
        self.assertEqual(self.cpu.x, 0x00)
        self.assertEqual(self.cpu.z, 1)
        self.assertEqual(self.cpu.n, 0)

    def test_dey(self):
        self.cpu.y = 0x01
        self.cpu.dey(None)
        self.assertEqual(self.cpu.y, 0x00)
        self.assertEqual(self.cpu.z, 1)
        self.assertEqual(self.cpu.n, 0)


if __name__ == '__main__':
    unittest.main()
