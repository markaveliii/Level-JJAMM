# This is for moving any animate creature in Level-JJAMM in the map

def move(map, creature, ix, iy, fx, fy):
    map.objArr[ix, iy] = '-'
    map.objArr[fx, fy] = creature
    return map
