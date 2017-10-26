import yaml

from nes.alu import Alu
from nes.clock import ClockListener
from .cycle import Cycle
from .instruction_decoder import InstructionDecoder
from .interrupt_vector import InterruptVector
from .microinstructions import Read, Increment, Move, AddressBusSelect
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
        self.timing = 0
        self.address_bus_selector = None

    @classmethod
    def create(cls, filename, nes):
        with open(filename, 'rt') as stream:
            yaml_data = yaml.load(stream)
            return Cpu(yaml_data, nes)

    def power_on(self):
        self.registers['PCL'].contents = 0x00
        self.registers['PCH'].contents = 0xC0

    def reset(self):
        self.pipeline = []
        self.pipeline.append(Cycle([AddressBusSelect('RES_LO'), Read()]))
        self.pipeline.append(Cycle([Move('DL', 'PCL'), AddressBusSelect('RES_HI'), Read()]))
        self.pipeline.append(Cycle([Move('DL', 'PCH')]))

    def irq(self):
        pass

    def nmi(self):
        pass

    def clock_event(self, event_name):
        if event_name == 'cycle-start':
            self.timing += 1

            if not self.pipeline:
                self.timing = 0
                self.fetch()

            cycle = self.pipeline.pop(0)

            cycle.execute(cpu=self)

            self.set_address_bus(self.address_bus_selector)

            if self.buses['R/W'].get() == 0:
                # Write
                self.buses['DB'].put(self.registers['DL'].contents)

        elif event_name == 'db-ready':
            if self.buses['R/W'].get() == 1:
                # Read
                self.registers['DL'].contents = self.buses['DB'].get()

                if self.timing == 0:
                    self.registers['IR'].contents = self.buses['DB'].get()
                    self.decode()

    def fetch(self):
        self.pipeline.append(Cycle([AddressBusSelect('PCX'), Read(), Increment('PCL')]))

    def decode(self):
        opcode = self.registers['IR'].contents
        instruction = self.decoder.get_instruction(opcode)
        addressing_mode = self.decoder.get_addressing_mode(opcode)
        self.pipeline.extend(addressing_mode.cycles)
        self.pipeline.extend(instruction.cycles)

    def set_address_bus(self, selector):
        if selector == 'PCX':
            addr_lo = self.registers['PCL'].contents
            addr_hi = self.registers['PCH'].contents
            addr = (addr_hi << 8) | addr_lo
        elif selector == 'ADX':
            addr_lo = self.registers['ADL'].contents
            addr_hi = self.registers['ADH'].contents
            addr = (addr_hi << 8) | addr_lo
        elif selector == 'BAX':
            addr_lo = self.registers['BAL'].contents
            addr_hi = self.registers['BAH'].contents
            addr = (addr_hi << 8) | addr_lo
        elif selector == 'AD_ZERO':
            addr_lo = self.registers['ADL'].contents
            addr_hi = 0x00
            addr = (addr_hi << 8) | addr_lo
        elif selector == 'BA_ZERO':
            addr_lo = self.registers['BAL'].contents
            addr_hi = 0x00
            addr = (addr_hi << 8) | addr_lo
        elif selector == 'STACK':
            addr_lo = self.registers['S'].contents
            addr_hi = 0x01
            addr = (addr_hi << 8) | addr_lo
        elif selector == 'NMI_LO':
            addr = self.vectors['NMI'].lo
        elif selector == 'NMI_HI':
            addr = self.vectors['NMI'].hi
        elif selector == 'RES_LO':
            addr = self.vectors['RESET'].lo
        elif selector == 'RES_HI':
            addr = self.vectors['RESET'].hi
        elif selector == 'IRQ_LO':
            addr = self.vectors['IRQ/BRK'].lo
        elif selector == 'IRQ_HI':
            addr = self.vectors['IRQ/BRK'].hi
        else:
            raise ValueError('Invalid Address Bus Selector: ' + self.address_bus_selector)

        self.buses['AB'].put(addr)
