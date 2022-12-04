def unpack(str):
    dims = str.split('x')
    l = int(dims[0])
    w = int(dims[1])
    h = int(dims[2])

    return l ,w ,h


def surfaceArea(l, w, h):
    lw = 2 * l * w 
    wh = 2 * w * h
    hl = 2 * h * l

    sideOne = l * w
    sideTwo = w * h
    sideThr = h * l

    minSide = min(sideOne, sideTwo, sideThr)

    return lw + wh + hl + minSide


def smallestPerim(l, w ,h):
    mins = sorted(tuple((l, w, h)))

    bow = mins[0] + mins[0] + mins[1] + mins[1]

    bow += l * w * h
    return bow


totalWrapping = 0
totalBow = 0
with open('src.txt') as f:
    data = f.readlines()

for line in data:
    l, w, h = unpack(line.strip())
    print(l, w, h)
    totalWrapping += surfaceArea(l, w, h)
    totalBow += smallestPerim(l, w, h)


print(f"part one = {totalWrapping}")
print(f"part two = {totalBow}")