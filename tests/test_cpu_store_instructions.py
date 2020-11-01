import unittest
from nes.processors.cpu import Cpu
from nes.bus import Bus
from nes.bus.devices.memory import Ram


class CpuStoreInstructionsTestCase(unittest.TestCase):
    def setUp(self):
        bus = Bus()
        bus.attach_device('RAM', Ram(256), 0, 256)
        self.cpu = Cpu(bus)
        self.cpu.write(0x0000, 0x00)

    def test_sta(self):
        self.cpu.a.value = 0xff
        instruction = self.cpu.decode(0x8D)
        instruction.parameter = 0x0000
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.read(0x0000), 0xff)

    def test_stx(self):
        self.cpu.x.value = 0xff
        instruction = self.cpu.decode(0x8E)
        instruction.parameter = 0x0000
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.read(0x0000), 0xff)

    def test_sty(self):
        self.cpu.y.value = 0xff
        instruction = self.cpu.decode(0x8C)
        instruction.parameter = 0x0000
        self.cpu.execute(instruction)
        self.assertEqual(self.cpu.read(0x0000), 0xff)


if __name__ == '__main__':
    unittest.main()
