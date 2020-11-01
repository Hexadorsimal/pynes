import unittest
from nes.processors.cpu import Cpu
from nes.bus import Bus
from nes.bus.devices.memory import Ram


class CpuDecrementInstructionsTestCase(unittest.TestCase):
    def setUp(self):
        bus = Bus()
        bus.attach_device('RAM', Ram(256), 0, 256)
        self.cpu = Cpu(bus)

    def test_dec(self):
        self.cpu.write(0x0000, 0x01)
        instruction = self.cpu.decode(0xCE)
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.read(0x0000), 0x00)
        self.assertTrue(self.cpu.p.z)
        self.assertFalse(self.cpu.p.n)

    def test_dex(self):
        self.cpu.x.value = 0x01
        instruction = self.cpu.decode(0xCA)
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.x.value, 0x00)
        self.assertTrue(self.cpu.p.z)
        self.assertFalse(self.cpu.p.n)

    def test_dey(self):
        self.cpu.y.value = 0x01
        instruction = self.cpu.decode(0x88)
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.y.value, 0x00)
        self.assertTrue(self.cpu.p.z)
        self.assertFalse(self.cpu.p.n)


if __name__ == '__main__':
    unittest.main()
