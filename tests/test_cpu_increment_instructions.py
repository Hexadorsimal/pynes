import unittest
from nes.processors.cpu import Cpu
from nes.bus import Bus
from nes.bus.devices.memory import Ram


class CpuIncrementInstructionsTestCase(unittest.TestCase):
    def setUp(self):
        bus = Bus()
        bus.attach_device('RAM', Ram(256), 0, 256)
        self.cpu = Cpu(bus)

    def test_inc(self):
        self.cpu.write(0x0000, 0x00)
        instruction = self.cpu.decode(0xEE)
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.read(0x0000), 0x01)
        self.assertFalse(self.cpu.p.z)
        self.assertFalse(self.cpu.p.n)

    def test_inx(self):
        self.cpu.x.value = 0x00
        instruction = self.cpu.decode(0xE8)
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.x.value, 0x01)
        self.assertFalse(self.cpu.p.z)
        self.assertFalse(self.cpu.p.n)

    def test_iny(self):
        self.cpu.y.value = 0x00
        instruction = self.cpu.decode(0xC8)
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.y.value, 0x01)
        self.assertFalse(self.cpu.p.z)
        self.assertFalse(self.cpu.p.n)


if __name__ == '__main__':
    unittest.main()
