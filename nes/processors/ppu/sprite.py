class Sprite:
    def __init__(self, data):
        self.data = data
        
    @property
    def y_position(self):
        return self.data[0]

    @property
    def x_position(self):
        return self.data[3]

    @property
    def tile_bank(self):
        return self.data[1] & 0x01
    
    @property
    def tile_number(self):
        return self.data[1] >> 1

    @property
    def palette(self):
        return self.data[2] & 0b00000011

    @property
    def priority(self):
        if self.data[2] & 0b00100000:
            return 'behind background'
        else:
            return 'in front of background'

    @property
    def flip_horizontal(self):
        return self.data[2] & 0b01000000

    @property
    def flip_vertical(self):
        return self.data[2] & 0b10000000
