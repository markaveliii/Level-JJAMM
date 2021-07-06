import curses
from curses import wrapper

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
                # print(x)
                # print('[',x,'][',y,']: ', end = '')
                # print(tile[x][y])
                print(self.tileArr[y][x], end = '')
            print()

    def printObjLets(self):
        for y in range(self.maxX):
            #print(y)
            for x in range(self.maxY):
                # print(x)
                # print('[',x,'][',y,']: ', end = '')
                # print(tile[x][y])
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
        # print('maxY: ', maxY)
        # print('maxX: ', maxX)
        self.tileArr = [[0 for y in range(self.maxY+1)] for x in range(self.maxX)] # https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
        self.objArr = [[0 for y in range(self.maxY+1)] for x in range(self.maxX)] # https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
        y = 0
        x = 0
        curFile.seek(0) # https://www.tutorialspoint.com/How-to-use-seek-method-to-reset-a-file-read-write-position-in-Python
        for line in curFile:
            x = 0
            # print(line)
            if line != '\n':
                for character in line:
                    self.tileArr[y][x] = character
                    # print('[',y,'][',x,']: ',self.tileArr[y][x])
                    x += 1
                y += 1
            else:
                break
        y = 0
        for line in curFile:
            x = 0
            # print(line)
            if line != '\n':
                for character in line:
                    self.objArr[y][x] = character
                    # print('[',y,'][',x,']: ',tile[y][x])
                    x += 1
                y += 1
            else:
                break

        for line in curFile:
            for character in line:
                if character != '\n':
                    self.winCond = character
        #return tile, obj, maxY, maxX


    def switchCase(self, obj):
        if obj.isupper():
            return obj, 7
        elif obj == '1':
            return 'X', 1

        elif obj == 's':
            return '|', 5

        elif obj == 'b':
            return 'M', 5

        elif obj == 'p':
            return 'U', 2

        elif obj == 'k':
            return 'P', 3

        elif obj == 'e':
            return 'O', 6

        elif obj == 'w':
            return ' ', 7

        else:
            return ' ', 4


    def displayMap(self):
        print('in displayMap: ')
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
                symbol, color = self.switchCase(self.objArr[y][x])
                stdscr.addstr(y, x, symbol, curses.color_pair(color))
        while True:
            c = stdscr.getch()
            if c == ord('q'):
                break
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
                                

        stdscr.clear()
        stdscr.refresh()

        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()



if __name__ == "__main__":

    # inFile = input('input the map file: ')
    mapObj = Map()
    inFile = []
    inFile.append('lvDebug.txt')
    inFile.append('lv1.txt')
    inFile.append('lv2.txt')

    fileNum = 0
    for fi in inFile:

        # tileArr, objArr, maxY, maxX = loadMap(inFile[fileNum])
        mapObj.loadMap(inFile[fileNum])
        print('maxY: ', mapObj.maxY)
        print('maxX: ', mapObj.maxX)
        print('winCond: ', mapObj.winCond)
        # print(tileArr)
        # print(objArr)

        #printTileLets(tileArr, maxY, maxX)
        mapObj.printTileLets()
        print()
        #printObjLets(objArr, maxY, maxX)
        mapObj.printObjLets()
        # curses.wrapper(mapObj.displayMap)
        mapObj.displayMap()
        fileNum += 1


'''
for yval in tile:
    for xval in yval:
        print(xval, end = '')
    print()
'''
