class Player:
    inventory = []

    def __init__(self, y_pos, x_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    #check inventory for sword
    def get_sword(self):
        found = False
        for item in self.inventory:
            if item == 'sword':
                found = True
        return found

    #insert sword into inventory
    def set_sword(self):
        self.inventory.append('sword')

    #moves players x,y position on map
    def move(self, keystroke, mapObj):
        if keystroke == 'w':
            if self.y_pos-1 <= 0:
                return
            dest = mapObj.objArr[self.y_pos-1][self.x_pos]
            if dest == 'w' or dest.isupper():
                return
            else:
                mapObj.objArr[self.y_pos][self.x_pos] = '-'
                self.y_pos -= 1
                mapObj.objArr[self.y_pos][self.x_pos] = 'p'

        elif keystroke == 'a':
            if self.x_pos-1 <= 0:
                return
            dest = mapObj.objArr[self.y_pos][self.x_pos-1]
            if dest == 'w' or dest.isupper():
                return
            else:
                mapObj.objArr[self.y_pos][self.x_pos] = '-'
                self.x_pos -= 1
                mapObj.objArr[self.y_pos][self.x_pos] = 'p'


        elif keystroke == 's':
            if self.y_pos+1 >= mapObj.maxY:
                return
            dest = mapObj.objArr[self.y_pos+1][self.x_pos]
            if dest == 'w' or dest.isupper():
                return
            else:
                mapObj.objArr[self.y_pos][self.x_pos] = '-'
                self.y_pos += 1
                mapObj.objArr[self.y_pos][self.x_pos] = 'p'


        elif keystroke == 'd':
            if self.x_pos+1 >= mapObj.maxX:
                return
            dest = mapObj.objArr[self.y_pos][self.x_pos+1]
            if dest == 'w' or dest.isupper():
                return
            else:
                mapObj.objArr[self.y_pos][self.x_pos] = '-'
                self.x_pos += 1
                mapObj.objArr[self.y_pos][self.x_pos] = 'p'


        mapObj.displayMap()
