from nes.registers.register import Register


class PpuScroll(Register):
    def __init__(self, scroll_x=0, scroll_y=0):
        self.scroll_x = scroll_x
        self.scroll_y = scroll_y
        self.write_to_x = True

    def write(self, data):
        if self.write_to_x:
            self.scroll_x = data
        else:
            self.scroll_y = data

        self.write_to_x = not self.write_to_x
