import yaml

from nes.alu import Alu
from nes.clock import ClockListener
from nes.memory import AbsoluteAddress, VectorAddress
from .instruction_decoder import InstructionDecoder
from .interrupt_vector import InterruptVector
from .microinstructions import Read, Increment
from .registers import RegisterFactory


class Cpu(ClockListener):
    def __init__(self, yaml_data, nes):
        self.registers = {}
        for register_data in yaml_data['registers']:
            register = RegisterFactory.create_register(register_data)
            self.registers[register.name] = register

        self.vectors = {}
        for vector_data in yaml_data['interrupt_vectors']:
            vector = InterruptVector(**vector_data)
            self.vectors[vector.name] = vector

        self.buses = {}
        for bus_data in yaml_data['buses']:
            name = bus_data['name']
            self.buses[name] = nes.buses[name]

        self.alu = Alu()
        self.decoder = InstructionDecoder()
        self.pipeline = []

    @classmethod
    def create(cls, filename, nes):
        with open(filename, 'rt') as stream:
            yaml_data = yaml.load(stream)
            return Cpu(yaml_data, nes)

    def power_on(self):
        self.registers['PCL'].contents = 0x00
        self.registers['PCH'].contents = 0xC0

    def reset(self):
        Read(VectorAddress('RESET', 0), 'PCL').execute(self)
        Read(VectorAddress('RESET', 1), 'PCH').execute(self)

    def irq(self):
        pass

    def nmi(self):
        pass

    def clock_tick(self, event_name):
        if event_name == 'phase 1':
            if not self.pipeline:
                self.fetch()
                self.decode()

            cycle = self.pipeline.pop(0)

            addr_lo = self.registers['ADL'].contents
            addr_hi = self.registers['ADH'].contents
            addr = (addr_hi << 8) | addr_lo
            self.buses['AB'].put(addr)
            self.buses['R/W'].put(cycle.read_write)

            cycle.execute(cpu=self)

        elif event_name == 'phase 2':
            if self.buses['R/W'].get() == 'write':
                self.buses['DB'].put(self.registers['DL'].contents)

        elif event_name == 'cycle complete':
            if self.buses['R/W'].get() == 'read':
                self.registers['DL'].contents = self.buses['DB'].get()

    def fetch(self):
        Read(AbsoluteAddress('PCH', 'PCL'), 'IR').execute(self)
        Increment('PCL').execute(self)

    def decode(self):
        instruction = self.decoder.get_instruction(self.registers['IR'].contents)
        self.pipeline.extend(instruction.cycles)
