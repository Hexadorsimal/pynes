import pytest
from nes.processors.cpu import Cpu
from nes.bus import Bus
from nes.bus.devices.memory import Ram
from nes.processors.cpu.decoder import Decoder
from nes.processors.instructions import factory


@pytest.fixture
def bus():
    bus = Bus()
    bus.attach_device('RAM', Ram(256), 0, 256)
    return bus

@pytest.fixture
def cpu(bus):
    return Cpu(bus, factory)

@pytest.fixture
def decoder():
    return Decoder()

@pytest.fixture
def lda(decoder):
    return decoder.decode(0xAD)


class TestCpuLoadInstructions:
    def test_lda(self, cpu, lda):
        cpu.write(0x0000, 0xff)

        instruction = factory.create(lda, [0x00, 0x00])
        instruction.execute(cpu)

        assert cpu.a == 0xff
        assert cpu.p.z is False
        assert cpu.p.n is True

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

