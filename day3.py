houses = {}

def deliver(directions):
    #houses = {}
    x = y= 0
    for dir in range(0, len(directions)):
        if directions[dir] == '^':
            y += 1
        elif directions[dir] == 'v':
            y -= 1
        elif directions[dir] == '>':
            x += 1
        elif directions[dir] == '<':
            x -= 1

        dkey = f'{str(x)},{str(y)}'
        if dkey in houses.keys():
            houses[dkey] = houses.get(dkey) + 1
        else:
            houses[dkey] = 1
    return


def part2(directions):
    santa = robot = ''
    for x in range(0,len(directions)):
        if x % 2 == 0:
            santa = santa + directions[x]
        else:
            robot = robot + directions[x]
    deliver(santa)
    deliver(robot)
    return (len(houses))


if __name__ == '__main__':
    with open('./inputs/day3.txt') as f:
        directions = f.readline()
    
    # part 1
    deliver(directions)
    print(len(houses)+1)
    houses.clear()
    #directions = '^>v<'
    print(part2(directions))