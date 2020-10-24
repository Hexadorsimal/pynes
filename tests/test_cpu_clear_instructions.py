import unittest
from nes.processors.cpu import Cpu
from nes.memory import Ram


class CpuClearInstructionsTestCase(unittest.TestCase):
    def setUp(self):
        ram = Ram(256)
        self.cpu = Cpu(ram)

    def test_clc(self):
        self.cpu.clc(None)
        self.assertEqual(self.cpu.c, 0)

    def test_cld(self):
        self.cpu.cld(None)
        self.assertEqual(self.cpu.d, 0)

    def test_cli(self):
        self.cpu.cli(None)
        self.assertEqual(self.cpu.i, 0)

    def test_clv(self):
        self.cpu.cli(None)
        self.assertEqual(self.cpu.v, 0)


if __name__ == '__main__':
    unittest.main()
