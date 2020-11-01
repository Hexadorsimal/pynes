import unittest
from nes.processors.cpu import Cpu
from nes.bus import Bus
from nes.bus.devices.memory import Ram


class CpuLoadInstructionsTestCase(unittest.TestCase):
    def setUp(self):
        bus = Bus()
        bus.attach_device('RAM', Ram(256), 0, 256)
        self.cpu = Cpu(bus)
        self.cpu.write(0x0000, 0xff)

    def test_lda(self):
        instruction = self.cpu.decode(0xAD)
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.a.value, 0xFF)
        self.assertFalse(self.cpu.p.z)
        self.assertTrue(self.cpu.p.n)

    def test_ldx(self):
        instruction = self.cpu.decode(0xAE)
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.x.value, 0xFF)
        self.assertFalse(self.cpu.p.z)
        self.assertTrue(self.cpu.p.n)

    def test_ldy(self):
        instruction = self.cpu.decode(0xAC)
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.y.value, 0xFF)
        self.assertFalse(self.cpu.p.z)
        self.assertTrue(self.cpu.p.n)


if __name__ == '__main__':
    unittest.main()
