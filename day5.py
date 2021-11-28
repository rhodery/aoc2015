import re

def part1(values):
    vowels = r'[aeiou]'
    double = r'(\w)\1'
    nostr = r'(ab|cd|pq|xy)'
    return len([True for item in values if not re.search(nostr, item) and len(re.findall(vowels, item)) >= 3 and re.search(double, item)])


def part2(values):
    repeat1 = r'(\w).\1'
    repeat2 = r'(\w\w).*\1'
    return len([True for item in values if re.search(repeat1, item) and re.search(repeat2, item)])


if __name__ == '__main__':
    nice = 0

    with open('./inputs/day5.txt') as f:
        kidlist = [line.rstrip('\n') for line in f.readlines()]

    print(part1(kidlist))
    print(part2(kidlist))