import curses
from curses import wrapper
#import os

class Map:
    tileArr = []
    objArr = []
    maxY = 0
    maxX = 0
    winCond = 'L'
    
    def printTileLets(self):
        for y in range(self.maxX):
            #print(y)
            for x in range(self.maxY):
                print(self.tileArr[y][x], end = '')
            print()

    def printObjLets(self):
        for y in range(self.maxX):
            #print(y)
            for x in range(self.maxY):
                print(self.objArr[y][x], end = '')
            print()


    def loadMap(self, inFile):
        curFile = open(inFile, 'r')
        self.maxY = len(curFile.readline()) - 1
        self.maxX = 0
        for line in curFile:
            if line != '\n':
                self.maxX += 1
            else:
                break
        self.maxX += 1
        self.tileArr = [[0 for y in range(self.maxY+1)] for x in range(self.maxX)] # https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
        self.objArr = [[0 for y in range(self.maxY+1)] for x in range(self.maxX)] # https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
        y = 0
        x = 0
        curFile.seek(0) # https://www.tutorialspoint.com/How-to-use-seek-method-to-reset-a-file-read-write-position-in-Python
        for line in curFile:
            x = 0
            if line != '\n':
                for character in line:
                    self.tileArr[y][x] = character
                    x += 1
                y += 1
            else:
                break
        y = 0
        for line in curFile:
            x = 0
            if line != '\n':
                for character in line:
                    self.objArr[y][x] = character
                    x += 1
                y += 1
            else:
                break

        for line in curFile:
            for character in line:
                if character != '\n':
                    self.winCond = character


    def mapSwitch(self, obj):
        if obj.isupper():
            return obj, 7
        elif obj == '1':
            return 'X', 1

        elif obj == 's':
            return '|', 5

        elif obj == 'b':
            return 'M', 5

        elif obj == 'p':
            return ' ', 2

        elif obj == 'k':
            return ' ', 3

        elif obj == 'e':
            return ' ', 6

        elif obj == 'w':
            return ' ', 7

        else:
            return ' ', 4


    def displayMap(self):
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        winY = curses.LINES - 1
        winX = curses.COLS - 1

        win = curses.newwin(winY, winX, 0, 0)
        curses.start_color()
        # curses.init_pair(0, curses.COLOR_BLACK, curses.COLOR_BLACK)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLUE)
        curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
        curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_CYAN)
        curses.init_pair(7, curses.COLOR_RED, curses.COLOR_BLACK)

        for y in range(self.maxX):
            for x in range(self.maxY):
                symbol, color = self.mapSwitch(self.objArr[y][x])
                stdscr.addstr(y, x, symbol, curses.color_pair(color))
        while True:
            c = stdscr.getch()
            if c == ord('q'):
                break

        stdscr.clear()
        stdscr.refresh()

        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()

        '''
        switch (self.objArr[y][x]){
                case '-':
                default:
                    stdscr.addstr(y, x, ' ', curses.color_pair(4))
                    break
                case '1':
                    stdscr.addstr(y, x, 'X', curses.color_pair(1))
                    break
                case 's':
                    stdscr.addstr(y, x, '|', curses.color_pair(5))
                    break
                case 'b':
                    stdscr.addstr(y, x, 'M', curses.color_pair(5))
                    break
                case 'p':
                    stdscr.addstr(y, x, 'U', curses.color_pair(2))
                    break
                case 'k':
                    stdscr.addstr(y, x, 'P', curses.color_pair(3))
                    break
                case 'e':
                    stdscr.addstr(y, x, 'O', curses.color_pair(6))
                    break
                case 'w':
                    stdscr.addstr(y, x, ' ', curses.color_pair(0))
                    break
            } # End of Switch statements
            '''
                                






'''
for yval in tile:
    for xval in yval:
        print(xval, end = '')
    print()
'''
