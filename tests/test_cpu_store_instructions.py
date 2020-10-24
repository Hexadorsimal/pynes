import unittest
from nes.processors.cpu import Cpu
from nes.memory import Ram


class CpuStoreInstructionsTestCase(unittest.TestCase):
    def setUp(self):
        self.ram = Ram(256)
        self.cpu = Cpu(self.ram)
        self.ram.write(0x0000, 0x00)

    def test_sta(self):
        self.cpu.a = 0xff
        self.cpu.sta(0x0000)
        self.assertEqual(self.ram.read(0x0000), 0xff)

    def test_stx(self):
        self.cpu.x = 0xff
        self.cpu.stx(0x0000)
        self.assertEqual(self.ram.read(0x0000), 0xff)

    def test_sty(self):
        self.cpu.y = 0xff
        self.cpu.sty(0x0000)
        self.assertEqual(self.ram.read(0x0000), 0xff)


if __name__ == '__main__':
    unittest.main()
