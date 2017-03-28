import os
import yaml
from app import db
from app.model import AddressingMode, Flag, Instruction, OpCode, Register, SignalLine


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
        with open(filename, 'r') as stream:
            yaml_data = yaml.load(stream)
            for register_dict in yaml_data["registers"]:
                register = Register(name=register_dict.get("name"),
                                    description=register_dict.get("description"),
                                    type=register_dict.get("type"))
                db.session.add(register)
                db.session.commit()

                if "flags" in register_dict:
                    for flag_dict in register_dict.get("flags"):
                        flag = Flag(letter=flag_dict.get("letter"),
                                    name=flag_dict.get("name"),
                                    description=flag_dict.get("description"),
                                    mask=flag_dict.get("mask"),
                                    register_id=register.id)
                        db.session.add(flag)
                        db.session.commit()

    def import_signal_lines(self, filename):
        with open(filename, 'r') as stream:
            yaml_data = yaml.load(stream)
            for signal_dict in yaml_data["signals"]:
                signal_line = SignalLine(name=signal_dict.get("name"),
                                         description=signal_dict.get("description"))
                db.session.add(signal_line)
            db.session.commit()

    def import_instruction(self, name, description):
        instruction = Instruction.query.filter_by(name=name).first()
        if not instruction:
            instruction = Instruction(name=name, description=description)
            db.session.add(instruction)
            db.session.commit()
        return instruction

    def import_instructions(self, instruction_dir):
        instruction_files = os.listdir(instruction_dir)
        for filename in instruction_files:
            with open(os.path.join(instruction_dir, filename)) as stream:
                yaml_data = yaml.load(stream)
                for instruction_dict in yaml_data["instructions"]:
                    instruction = self.import_instruction(instruction_dict["name"], instruction_dict["description"])

                    for opcode_dict in instruction_dict["opcodes"]:
                        hex_opcode_string = str(opcode_dict["hex"])
                        code = int(hex_opcode_string, base=16)

                        addressing_mode = AddressingMode.query.filter_by(name=opcode_dict["mode"]).first()

                        opcode = OpCode(id=code,
                                        addressing_mode_id=addressing_mode.id,
                                        instruction_id=instruction.id)
                        db.session.add(opcode)
        db.session.commit()
