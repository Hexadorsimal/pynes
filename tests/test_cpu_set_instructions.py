import unittest
from nes.cpu import Cpu
from nes.memory import Ram


class CpuSetInstructionsTestCase(unittest.TestCase):
    def setUp(self):
        ram = Ram(256)
        self.cpu = Cpu(ram)

    def test_sec(self):
        self.cpu.sec(None)
        self.assertEqual(self.cpu.c, 1)

    def test_sed(self):
        self.cpu.sed(None)
        self.assertEqual(self.cpu.d, 1)

    def test_sei(self):
        self.cpu.sei(None)
        self.assertEqual(self.cpu.i, 1)


if __name__ == '__main__':
    unittest.main()
