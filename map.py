if __name__ == "__main__":

    # inFile = input('input the map file: ')
    inFile = 'lv1.txt'
    curFile = open(inFile, 'r')
    maxY = len(curFile.readline()) - 1
    maxX = 0
    for line in curFile:
        if line != '\n':
            maxX += 1
        else:
            break
    maxX += 1
    print('maxY: ', maxY)
    print('maxX: ', maxX)
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

    
    y = 0
    x = 0
    for x in range(maxX):
        #print(y)
        for y in range(maxY):
            # print(x)
            # print('[',x,'][',y,']: ', end = '')
            # print(tile[x][y])
            print(tile[x][y], end = '')
        print()

    print()

    for x in range(maxX):
        #print(y)
        for y in range(maxY):
            # print(x)
            # print('[',x,'][',y,']: ', end = '')
            # print(tile[x][y])
            print(obj[x][y], end = '')
        print()


    '''
    for yval in tile:
        for xval in yval:
            print(xval, end = '')
        print()
    '''
