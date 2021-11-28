if __name__ == '__main__':

    with open('./inputs/day1.txt') as f:
        steps = f.readline()

    # part 1
    floor = steps.count('(') - steps.count(')')
    print(floor)

    # part 2
    pos = 0
    for x in range(len(steps)):
        if steps[x] == '(':
            pos += 1
        elif steps[x] == ')':
            pos -= 1
        if pos < 0:
            print(x+1)
            break
