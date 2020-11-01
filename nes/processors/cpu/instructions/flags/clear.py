from .flag import FlagInstruction


class ClearInstruction(FlagInstruction):
    def execute(self, processor):
        processor.p.flags[self.flag_name].clear()
