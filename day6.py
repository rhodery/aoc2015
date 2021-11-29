import re
from collections import defaultdict

def part_one(coord_list) -> int:
    lights_on = set()
    for coord in coord_list:
        switch = re.search(r'(on|off|toggle)', coord).group()
        x1, y1, x2, y2 = list(map(int, re.findall(r'\d+', coord)))
        modify = {(x,y) for x in range(x1, x2+1) for y in range(y1, y2+1)}
        if switch == 'on':
            lights_on.update(modify)
        elif switch == 'off':
            lights_on.difference_update(modify)
        elif switch == 'toggle':
            lights_to_toggle = modify.difference(lights_on)
            lights_on.difference_update(modify)
            lights_on.update(lights_to_toggle)
    return len(lights_on)


def part_two(coord_list) -> int:
    lights = defaultdict(int)
    for coord in coord_list:
        switch = re.search(r'(on|off|toggle)', coord).group()
        x1, y1, x2, y2 = list(map(int, re.findall(r'\d+', coord)))
        modify = {(x,y) for x in range(x1, x2+1) for y in range(y1, y2+1)}

        for light in modify:
            if switch == 'on':
                lights[light] += 1
            elif switch == 'off':
                if lights[light]:
                    lights[light] -= 1
            elif switch == 'toggle':
                lights[light] += 2
    return sum(list(lights.values()))
    

if __name__ == '__main__':
    with open('./inputs/day6.txt') as f:
        coord_list = [line.strip() for line in f.readlines()]

    #print(f'{part_one(coord_list)}')
    print(f'{part_two(coord_list)}')