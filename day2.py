def calc(boxes):
    total = {}
    paper = 0
    ribbon = 0
    for box in boxes:
        box=list(map(int,box))
        box.sort()
        l,w,h = [box[x] for x in (0,1,2)]
        lw, wh, hl = l*w, w*h, h*l
        paper += 2*lw + 2*wh + 2*hl + min(lw,wh,hl)
        ribbon += (l+l+w+w) + (l*w*h)
    
    total['paper'] = paper
    total['ribbon'] = ribbon
    return total


if __name__ == '__main__':

    with open('./inputs/day2.txt') as f:
        boxes = [line.rstrip('\n').split('x') for line in f.readlines()]

    # part 1 & 2
    print(calc(boxes)['paper'])
    print(calc(boxes)['ribbon'])