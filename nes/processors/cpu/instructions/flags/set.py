from .flag import FlagInstruction


class SetInstruction(FlagInstruction):
    def execute(self, processor):
        processor.p.flags[self.flag_name].set()
