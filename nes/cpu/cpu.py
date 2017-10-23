import yaml

from .alu.alu_operations import AluIncrementOperation
from .instruction_decoder import InstructionDecoder
from .interrupt_vector import InterruptVector
from .operation import ReadOperation
from .register_factory import RegisterFactory
from ..memory.address import AbsoluteAddress, VectorAddress


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
        self.decoder = InstructionDecoder()
        self.pipeline = []

    @classmethod
    def create(cls, filename, nes):
        with open(filename, 'rt') as stream:
            yaml_data = yaml.load(stream)
            return Cpu(yaml_data, nes)

    def reset(self):
        ReadOperation(VectorAddress('RESET', 0), 'PCL').execute(self)
        ReadOperation(VectorAddress('RESET', 1), 'PCH').execute(self)
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
        ReadOperation(AbsoluteAddress('PCH', 'PCL'), 'IR').execute(self)
        AluIncrementOperation('PCL').execute(self)

    def decode(self):
        instruction = self.decoder.get_instruction(self.registers['IR'].contents)
        self.pipeline.extend(instruction.cycles)

    def execute(self):
        while self.pipeline:
            cycle = self.pipeline.pop(0)
            for operation in cycle.operations:
                operation.execute(self)
