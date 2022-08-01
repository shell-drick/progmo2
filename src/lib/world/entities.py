class Entity():

    def __init__(self):
        pass


class Block(Entity):
    
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y
        
    def get_pos(self):
        return (self.x_pos, self.y_pos)
    

class Minion(Entity):
    
    def __init__(self, owner):
        self.owner = owner
        self.energy = 5
        
    def get_pos(self):
        return (self.x, self.y)
    
    def set_pos(self, x_pos=None, y_pos=None):
        if x_pos:
            self.x_pos = x_pos
            
        if y_pos:
            self.y_pos = y_pos
            
            