
import player
# This is for moving any animate creature in Level-JJAMM in the map

def move(creature, keystroke):

    if keystroke == 'w':
        creature.y_pos -= 1
    elif keystroke == 'a':
        creature.x_pos -=1
    elif keystroke == 's':
        creature.y_pos += 1
    elif keystroke == 'd':
        creature.x_pos += 1

p1 = player.Player(0,0)
move(p1, 'w')

print(p1.x_pos, ", ", p1.y_pos)
