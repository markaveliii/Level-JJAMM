def printTileLets(tileArr, maxY, maxX):
    for x in range(maxX):
        #print(y)
        for y in range(maxY):
            # print(x)
            # print('[',x,'][',y,']: ', end = '')
            # print(tile[x][y])
            print(tileArr[x][y], end = '')
        print()

def printObjLets(objArr, maxY, maxX):
    for x in range(maxX):
        #print(y)
        for y in range(maxY):
            # print(x)
            # print('[',x,'][',y,']: ', end = '')
            # print(tile[x][y])
            print(objArr[x][y], end = '')
        print()


def loadMap(inFile):
    curFile = open(inFile, 'r')
    maxY = len(curFile.readline()) - 1
    maxX = 0
    for line in curFile:
        if line != '\n':
            maxX += 1
        else:
            break
    maxX += 1
    # print('maxY: ', maxY)
    # print('maxX: ', maxX)
    tile = [[0 for y in range(maxY+1)] for x in range(maxX)] # https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
    obj = [[0 for y in range(maxY+1)] for x in range(maxX)] # https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
    y = 0
    x = 0
    curFile.seek(0) # https://www.tutorialspoint.com/How-to-use-seek-method-to-reset-a-file-read-write-position-in-Python
    for line in curFile:
        x = 0
        # print(line)
        if line != '\n':
            for character in line:
                tile[y][x] = character
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
                obj[y][x] = character
                # print('[',y,'][',x,']: ',tile[y][x])
                x += 1
            y += 1
    return tile, obj, maxY, maxX

if __name__ == "__main__":

    # inFile = input('input the map file: ')
    inFile = []
    inFile.append('lv1.txt')
    inFile.append('lvl2.txt')

    fileNum = 0
    for fi in inFile:

        tileArr, objArr, maxY, maxX = loadMap(inFile[fileNum])
        print('maxY: ', maxY)
        print('maxX: ', maxX)
        # print(tileArr)
        # print(objArr)

        printTileLets(tileArr, maxY, maxX)
        print()
        printObjLets(objArr, maxY, maxX)
        fileNum += 1


    '''
    for yval in tile:
        for xval in yval:
            print(xval, end = '')
        print()
    '''
