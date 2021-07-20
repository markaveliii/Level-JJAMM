import time #found sleep function at https://www.tutorialspoint.com/python3/time_sleep.htm

class Player:
    inventory = []

    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.sword = False
        self.bow = False
        self.debug = False
        self.key = 0
        self.lives = 3
        self.equipped = None

    def debugMode(self):
        self.debug = True

    #check inventory for sword
    def get_sword(self):
        return self.sword

    #insert sword into inventory
    def set_sword(self):
        self.sword = True
        self.equipped = 'sword'

    #check inventory for bow
    def get_bow(self):
        return self.bow

    #insert bow into inventory
    def set_bow(self):
        self.bow = True
        self.equipped = 'bow'

    #check for equipped item
    def get_equipped(self):
        return self.equipped

    def swap_equipped(self, swap):
        self.equipped = swap

    #check for enemy in destination cell
    def enemy_there(self, dest):
        if dest == '1' or dest == '2' or dest == '3' or dest == '4':
            # print('you died')
            return True
        else:
            return False

    #check for item in destination cell
    def item_there(self, dest):
        if dest == 's':
            self.set_sword()
            return True
        elif dest == 'b':
            self.set_bow()
            return True
        elif dest == 'k':
            self.key += 1
            return True
        else:
            return False

    def move(self, keystroke, mapObj):
        desx = 0
        desy = 0
        # moving up
        if keystroke == 'w':
            desy = self.y_pos-1
            desx = self.x_pos

        #moving left
        elif keystroke == 'a':
            desy = self.y_pos
            desx = self.x_pos-1

        # moving down
        elif keystroke == 's':
            desy = self.y_pos+1
            desx = self.x_pos

        #moving right
        elif keystroke == 'd':
            desy = self.y_pos
            desx = self.x_pos+1

        

        #check for out of bounds movement
        if desx >= mapObj.maxX or desx < 0 or desy >= mapObj.maxY or desy < 0:
            return
            
        dest = mapObj.objArr[desy][desx]

        if dest == 'w' or dest.isupper():
             return
        elif self.enemy_there(dest):
            print('You died')
            mapObj.objArr[desy][desx] = 'd'
            mapObj.displayMap()
            mapObj.stdscr.refresh()
            time.sleep(1)
            mapObj.reset(self)
            mapObj.displayMap()
            return
        elif self.item_there(dest):
            print('You picked up the item!')
        elif dest == 'e':
            if mapObj.winCheck(self):
                mapObj.objArr[self.y_pos][self.x_pos] = '-'
                self.x_pos = desx
                self.y_pos = desy
                dest = 'p'
                mapObj.displayMap()
                mapObj.stdscr.refresh()
                time.sleep(1)
                return True


                        

        #updates objArr for map
        mapObj.objArr[desy][desx] = 'p'
        if not mapObj.initArr[self.y_pos][self.x_pos] == 'e':
            mapObj.objArr[self.y_pos][self.x_pos] = '-'
        else:
            mapObj.objArr[self.y_pos][self.x_pos] = 'e'
        self.x_pos = desx
        self.y_pos = desy


        mapObj.displayMap()
