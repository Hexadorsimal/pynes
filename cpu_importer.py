import os
import yaml
from cpu.connection import Connection
from cpu.counter import Counter
from cpu.flagregister import FlagRegister, StatusFlag
from cpu.register import Register
from app import db
from app.model import AddressingMode, Instruction


class CpuImporter:
    def __init__(self):
        self.registers = []
        self.connections = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def import_addressing_modes(self, filename):
        with open(filename) as stream:
            yaml_data = yaml.load(stream)
            for addressing_mode_dict in yaml_data["addressing_modes"]:
                name = addressing_mode_dict["name"]
                if name == "fetch":
                    continue
                addressing_mode = AddressingMode(name)
                db.session.add(addressing_mode)
            db.session.commit()

    def import_registers(self, filename):
        with open('cpu/6502.yaml', 'r') as stream:
            yaml_data = yaml.load(stream)
            for register_dict in yaml_data["registers"]:
                type = register_dict.pop("type", None)
                if type == "flags":
                    flags = []
                    for flag_dict in register_dict["flags"]:
                        flags.append(StatusFlag(**flag_dict))
                    register_dict["flags"] = flags
                    registers.append(FlagRegister(**register_dict))
                elif type == "accumulator" or type == "index":
                    registers.append(Counter(**register_dict))
                else:
                    registers.append(Register(**register_dict))

            for connection_dict in yaml_data["connections"]:
                connections.append(Connection(**connection_dict))

    def import_instructions(self, instruction_dir):
        instruction_files = os.listdir(instruction_dir)
        for filename in instruction_files:
            with open(os.path.join(instruction_dir, filename)) as stream:
                yaml_data = yaml.load(stream)
                for instruction_dict in yaml_data["instructions"]:
                    for opcode in instruction_dict["opcodes"]:
                        opcode_string = str(opcode["hex"])
                        hex_code = int(opcode_string, base=16)

                        addressing_mode = AddressingMode.query.filter_by(name=opcode["mode"]).first()

                        instruction = Instruction(id=hex_code,
                                                  addressing_mode_id=addressing_mode.id,
                                                  name=instruction_dict["name"],
                                                  description=instruction_dict["description"])
                        db.session.add(instruction)
        db.session.commit()
