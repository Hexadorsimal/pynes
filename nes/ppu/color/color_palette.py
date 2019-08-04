class ColorPalette:
    def __init__(self, colors):
        self.colors = colors

    @staticmethod
    def from_file(filename):
        colors = []

        with open(filename, 'rt') as f:
            lines = f.read().splitlines()

            for line in lines:
                r, g, b = line.split(',')
                color = (int(r, 16), int(g, 16), int(b, 16))
                colors.append(color)

        return ColorPalette(colors)
