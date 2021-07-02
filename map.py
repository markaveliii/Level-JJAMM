class Map:
    tileArr = []
    objArr = []
    maxY = 0
    maxX = 0
    winCond = 'L'
    
    def printTileLets(self):
        for x in range(self.maxX):
            #print(y)
            for y in range(self.maxY):
                # print(x)
                # print('[',x,'][',y,']: ', end = '')
                # print(tile[x][y])
                print(self.tileArr[x][y], end = '')
            print()

    def printObjLets(self):
        for x in range(self.maxX):
            #print(y)
            for y in range(self.maxY):
                # print(x)
                # print('[',x,'][',y,']: ', end = '')
                # print(tile[x][y])
                print(self.objArr[x][y], end = '')
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
                    # print('[',y,'][',x,']: ',tile[y][x])
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

if __name__ == "__main__":

    # inFile = input('input the map file: ')
    mapObj = Map()
    inFile = []
    inFile.append('lv1.txt')
    inFile.append('lvl2.txt')

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
        fileNum += 1


    '''
    for yval in tile:
        for xval in yval:
            print(xval, end = '')
        print()
    '''
