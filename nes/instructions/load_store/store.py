from nes.instructions import Instruction


class StoreInstruction(Instruction):
    register = None

    def execute(self, processor):
        self.write_result(processor, processor.registers[self.register].value)
