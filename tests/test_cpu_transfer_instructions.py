import unittest
from nes.processors.cpu import Cpu
from nes.bus import Bus
from nes.bus.devices.memory import Ram


class CpuTransferInstructionsTestCase(unittest.TestCase):
    def setUp(self):
        bus = Bus()
        bus.attach_device('Stack Area', Ram(0x100), 0x100, 0x100)
        self.cpu = Cpu(bus)

    def test_tax(self):
        self.cpu.a.value = 3
        instruction = self.cpu.decode(0xAA)
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.a.value, self.cpu.x.value)
        self.assertEqual(self.cpu.x.value, 3)

    def test_tay(self):
        self.cpu.a.value = 2
        instruction = self.cpu.decode(0xA8)
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.a.value, self.cpu.y.value)
        self.assertEqual(self.cpu.y.value, 2)

    def test_txa(self):
        self.cpu.x.value = 10
        instruction = self.cpu.decode(0x8A)
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.a.value, self.cpu.x.value)
        self.assertEqual(self.cpu.a.value, 10)

    def test_tya(self):
        self.cpu.y.value = 0xDD
        instruction = self.cpu.decode(0x98)
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.a.value, self.cpu.y.value)
        self.assertEqual(self.cpu.a.value, 0xDD)

    def test_tsx(self):
        self.cpu.s.value = 0xFD
        instruction = self.cpu.decode(0xBA)
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.x.value, 0xFD)

    def test_txs(self):
        self.cpu.x.value = 0xAA
        instruction = self.cpu.decode(0x9A)
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.s.value, 0xAA)


if __name__ == '__main__':
    unittest.main()
