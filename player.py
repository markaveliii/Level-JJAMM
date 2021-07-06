class Player:
	inventory = []

	def __init__(self, x_pos, y_pos):
	    self.x_pos = x_pos
	    self.y_pos = y_pos

        #check inventory for sword
        def get_sword(self):
            found = False
            for item in self.inventory:
                if item = 'sword':
                    found = True
            return found

        #insert sword into inventory
        def set_sword(self):
            self.inventory.append('sword')
