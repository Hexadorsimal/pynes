import unittest
from nes.cpu import Cpu
from nes.memory import Ram


class CpuTransferInstructionsTestCase(unittest.TestCase):
    def setUp(self):
        ram = Ram(256)
        self.cpu = Cpu(ram)
        self.cpu.x = 1
        self.cpu.y = 2
        self.cpu.a = 3
        self.cpu.s = 4

    def test_tax(self):
        self.cpu.tax(None)
        self.assertEqual(self.cpu.a, self.cpu.x)
        self.assertEqual(self.cpu.x, 3)

    def test_tay(self):
        self.cpu.tay(None)
        self.assertEqual(self.cpu.a, self.cpu.y)
        self.assertEqual(self.cpu.y, 3)

    def test_tsx(self):
        self.cpu.tsx(None)
        self.assertEqual(self.cpu.s, self.cpu.x)
        self.assertEqual(self.cpu.x, 4)

    def test_txa(self):
        self.cpu.txa(None)
        self.assertEqual(self.cpu.x, self.cpu.a)
        self.assertEqual(self.cpu.a, 1)

    def test_txs(self):
        self.cpu.txs(None)
        self.assertEqual(self.cpu.x, self.cpu.s)
        self.assertEqual(self.cpu.s, 1)

    def test_tya(self):
        self.cpu.tya(None)
        self.assertEqual(self.cpu.y, self.cpu.a)
        self.assertEqual(self.cpu.a, 2)


if __name__ == '__main__':
    unittest.main()
