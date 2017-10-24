import yaml

from nes.alu import Alu
from nes.memory import AbsoluteAddress, VectorAddress
from .instruction_decoder import InstructionDecoder
from .interrupt_vector import InterruptVector
from .microinstructions import ReadMicroinstruction, IncrementMicroinstruction
from .registers import RegisterFactory


class Cpu:
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

        self.memory = None
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
        self.run()

    def reset(self):
        ReadMicroinstruction(VectorAddress('RESET', 0), 'PCL').execute(self)
        ReadMicroinstruction(VectorAddress('RESET', 1), 'PCH').execute(self)
        self.run()

    def irq(self):
        pass

    def nmi(self):
        pass

    def run(self):
        while True:
            self.step()

    def step(self):
        self.fetch()
        self.decode()
        self.execute()

    def fetch(self):
        ReadMicroinstruction(AbsoluteAddress('PCH', 'PCL'), 'IR').execute(self)
        IncrementMicroinstruction('PCL').execute(self)

    def decode(self):
        instruction = self.decoder.get_instruction(self.registers['IR'].contents)
        self.pipeline.extend(instruction.cycles)

    def execute(self):
        while self.pipeline:
            cycle = self.pipeline.pop(0)
            for microinstruction in cycle.microinstructions:
                microinstruction.execute(self)
