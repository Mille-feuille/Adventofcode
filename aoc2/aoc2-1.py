def openfile(filename):
    ifile = open(filename)
    directions = []
    for line in ifile:
        directions.append(str.strip(line))
    ifile.close()
    return directions
    # directions = ifile.readline()
    # print(directions)


def checkbounds(mov):
    if mov < 0:
        return 0
    elif mov > 2:
        return 2
    else:
        return mov


def lineloop(instruct, x, y):
    orderedpairs = []
    for i in range(len(instruct)):
        for j in range(len(instruct[i])):
            if instruct[i][j] == 'U':
                y -= 1
                y = checkbounds(y)
            elif instruct[i][j] == 'D':
                y += 1
                y = checkbounds(y)
            elif instruct[i][j] == 'L':
                x -= 1
                x = checkbounds(x)
            elif instruct[i][j] == 'R':
                x += 1
                x = checkbounds(x)
        orderedpairs.append((x, y))
    return orderedpairs


def convertcoords(coordlist):
    keypad = [[1, 4, 7],
              [2, 5, 8],
              [3, 6, 9]]
    for i in range(len(coordlist)):
        tempx = coordlist[i][0]
        tempy = coordlist[i][1]
        print(keypad[tempx][tempy])


def main():
    x = 1
    y = 1

    instruct = openfile('aoc2-1.txt')
    finalnumbers = lineloop(instruct, x, y)
    convertcoords(finalnumbers)

main()
