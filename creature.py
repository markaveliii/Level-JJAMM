class creature:
    typ = 0
    xpos = 0
    ypos = 0
    alive = 1

    def __init__(self, typ, xpos, ypos):
        self.type = typ
        self.xpos = xpos
        self.ypos = ypos

    def movement(self, map):
        if(self.alive == 0):
            return 0
        if(typ == 0 or 1):
            return 1
        
    def dead(self):
        self.alive = 0
        return 1
    
    def status(self):
        return self.alive