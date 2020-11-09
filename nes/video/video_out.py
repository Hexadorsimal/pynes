class VideoOut:
    def power_up(self):
        pass

    def power_down(self):
        pass

    def pixel(self, x, y, color):
        raise NotImplementedError

    def hsync(self):
        raise NotImplementedError

    def vsync(self):
        raise NotImplementedError
