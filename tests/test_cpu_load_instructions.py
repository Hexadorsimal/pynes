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

@pytest.fixture
def ldx(decoder):
    return decoder.decode(0xAE)

@pytest.fixture
def ldy(decoder):
    return decoder.decode(0xAC)


class TestCpuLoadInstructions:
    def test_lda(self, cpu, lda):
        cpu.write(0x0000, 0xff)

        instruction = factory.create(lda, [0x00, 0x00])
        instruction.execute(cpu)

        assert cpu.a == 0xff
        assert cpu.p.z is False
        assert cpu.p.n is True

    def test_ldx(self, cpu, ldx):
        cpu.write(0x0000, 0xff)

        instruction = factory.create(ldx, [0x00, 0x00])
        instruction.execute(cpu)

        assert cpu.x == 0xff
        assert cpu.p.z is False
        assert cpu.p.n is True

    def test_ldy(self, cpu, ldy):
        cpu.write(0x0000, 0xff)

        instruction = factory.create(ldy, [0x00, 0x00])
        instruction.execute(cpu)

        assert cpu.y == 0xff
        assert cpu.p.z is False
        assert cpu.p.n is True

