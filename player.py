import time #found sleep function at https://www.tutorialspoint.com/python3/time_sleep.htm

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
            return True
        elif dest == 'k': # TODO: This will need to set key
            return True
        else:
            return False

    def move(self, keystroke, mapObj):
        # moving up
        if keystroke == 'w':
            #check for out of bounds movement
            if self.y_pos-1 <= 0:
                return

            #sets destination cell for processing
            dest = mapObj.objArr[self.y_pos-1][self.x_pos]
            if dest == 'w' or dest.isupper():
                return
            else:
                if self.enemy_there(dest):
                    print('You died')
                    mapObj.objArr[self.y_pos-1][self.x_pos] = 'd'
                    mapObj.displayMap()
                    mapObj.stdscr.refresh()
                    time.sleep(1)
                    mapObj.reset(self)
                    return
                if self.item_there(dest):
                    print('You picked up the item!')
                if dest == 'e':
                    if mapObj.winCheck():
                        mapObj.objArr[self.y_pos][self.x_pos] = '-'
                        self.y_pos -= 1
                        mapObj.objArr[self.y_pos][self.x_pos] = 'p'
                        mapObj.displayMap()
                        mapObj.stdscr.refresh()
                        time.sleep(1)
                        return True

                #updates objArr for map
                mapObj.objArr[self.y_pos][self.x_pos] = '-'
                self.y_pos -= 1
                mapObj.objArr[self.y_pos][self.x_pos] = 'p'
        #moving left
        elif keystroke == 'a':
            #check for out of bounds movement
            if self.x_pos-1 <= 0:
                return
            
            #sets destination cell for processing
            dest = mapObj.objArr[self.y_pos][self.x_pos-1]
            if dest == 'w' or dest.isupper():
                return
            else:
                if self.enemy_there(dest):
                    print('You died')
                    mapObj.objArr[self.y_pos][self.x_pos-1] = 'd'
                    mapObj.displayMap()
                    mapObj.stdscr.refresh()
                    time.sleep(1)
                    mapObj.reset(self)
                    return
                if self.item_there(dest):
                    print('You picked up the item!')
                if dest == 'e':
                    if mapObj.winCheck():
                        mapObj.objArr[self.y_pos][self.x_pos] = '-'
                        self.x_pos -= 1
                        mapObj.objArr[self.y_pos][self.x_pos] = 'p'
                        mapObj.displayMap()
                        mapObj.stdscr.refresh()
                        time.sleep(1)
                        return True

                #updates objArr for map
                mapObj.objArr[self.y_pos][self.x_pos] = '-'
                self.x_pos -= 1
                mapObj.objArr[self.y_pos][self.x_pos] = 'p'

        # moving down
        elif keystroke == 's':
            #check for out of bounds movement
            if self.y_pos+1 >= mapObj.maxY:
                return
            
            #sets destination cell for processing
            dest = mapObj.objArr[self.y_pos+1][self.x_pos]
            if dest == 'w' or dest.isupper():
                return
            else:
                if self.enemy_there(dest):
                    print('You died')
                    mapObj.objArr[self.y_pos+1][self.x_pos] = 'd'
                    mapObj.displayMap()
                    mapObj.stdscr.refresh()
                    time.sleep(1)
                    mapObj.reset(self)
                    return
                if self.item_there(dest):
                    print('You picked up the item!')
                if dest == 'e':
                    if mapObj.winCheck():
                        mapObj.objArr[self.y_pos][self.x_pos] = '-'
                        self.y_pos += 1
                        mapObj.objArr[self.y_pos][self.x_pos] = 'p'
                        mapObj.displayMap()
                        mapObj.stdscr.refresh()
                        time.sleep(1)
                        return True

                #updates objArr for map
                mapObj.objArr[self.y_pos][self.x_pos] = '-'
                self.y_pos += 1
                mapObj.objArr[self.y_pos][self.x_pos] = 'p'

        #moving right
        elif keystroke == 'd':
            #check for out of bounds movement
            if self.x_pos+1 >= mapObj.maxX:
                return
            
            #sets destination cell for processing
            dest = mapObj.objArr[self.y_pos][self.x_pos+1]
            if dest == 'w' or dest.isupper():
                return
            else:
                if self.enemy_there(dest):
                    print('You died')
                    mapObj.objArr[self.y_pos][self.x_pos+1] = 'd'
                    mapObj.displayMap()
                    mapObj.stdscr.refresh()
                    time.sleep(1)
                    mapObj.reset(self)
                    return
                if self.item_there(dest):
                    print('You picked up the item!')
                if dest == 'e':
                    if mapObj.winCheck():
                        mapObj.objArr[self.y_pos][self.x_pos] = '-'
                        self.x_pos += 1
                        mapObj.objArr[self.y_pos][self.x_pos+1] = 'p'
                        mapObj.displayMap()
                        mapObj.stdscr.refresh()
                        time.sleep(1)
                        return True
                        

                #updates objArr for map
                mapObj.objArr[self.y_pos][self.x_pos] = '-'
                self.x_pos += 1
                mapObj.objArr[self.y_pos][self.x_pos] = 'p'

        mapObj.displayMap()
