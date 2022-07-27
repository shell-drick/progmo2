from lib.world.entities import Block


class Tile():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def get_pos(self):
        return (self.x, self.y)

    def __repr__(self):
        return str(self.get_pos())

class WorldMap():
    
    def __init__(self, size: tuple):
        self.size = size
        data = []
        for y in range(size):
            for x in range(size):
                data += [ Tile(x, y) ]

        self.data = data
        
    def dump(self):
        return self.data

    def get_pos(self, x, y):
        return self.data[(y*self.size)+x]

    def set_tile(self, x, y, value):
        self.data[(y*self.size)+x] = value

    def create_block(self, x, y):
        self.set_tile(x, y, Block(x, y))
        pass
    
        
    
World = WorldMap(10)