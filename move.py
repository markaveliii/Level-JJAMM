# This is for moving any animate creature in Level-JJAMM in the map

def move(map, creature, ix, iy, fx, fy):
    map[ix, iy].creature = 0
    map[fx, fy].creature = 1
    return map