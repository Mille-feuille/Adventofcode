def main():
    facing = 0
    x = 0
    y = 0

    ifile = open('aoc1-1dir.csv')
    directions = (next(ifile).split(sep=', '))
    locations = []

    # print (directions)

    for i in directions:
        # print(i[0])
        if i[0] == 'R':
            facing += 1
        elif i[0] == 'L':
            facing -= 1

        facing = facing % 4
        templen = (i[1:])
        templen = int(templen)


        # print(i[1:])
        for i in range(templen):
            if facing == 0:
                y += 1
            elif facing == 1:
            #x += int(i[1:])
                x += 1
            elif facing == 2:
                y -= 1
            elif facing == 3:
                x -= 1
            locations.append((x, y))
            for i in locations:
                if locations.count(i) > 1:
                    distance = abs(x) + abs(y)
                    print(i)
                    print(distance)
                    return
#            x -= int(i[1:])
        # print(facing,x,y)

main()