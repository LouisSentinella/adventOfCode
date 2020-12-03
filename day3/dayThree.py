import time

start = time.time()

file = open("slope.txt", "r")
currentLocation = (0, 0)
slopeMap = []

for line in file:
    line = line.strip()
    slopeMap.append([location for location in line])


def tree_counter(xInc, yInc, slopeMap):
    finished = False
    y = 0
    x = 0
    treeCounter = 0
    while not finished:
        if y == len(slopeMap) - 1:
            finished = True
        else:
            x, y = x + xInc, y + yInc
            if x > len(slopeMap[0]) - 1:
                x -= len(slopeMap[0])
            if y > len(slopeMap):
                y -= len(slopeMap)
            if slopeMap[y][x] == '#':
                treeCounter += 1

    return treeCounter


def part_one(slopeMap):
    return tree_counter(3, 1, slopeMap)


def part_two(slopeMap):
    return tree_counter(1, 1, slopeMap) * tree_counter(3, 1, slopeMap) * tree_counter(5, 1, slopeMap) * tree_counter(7, 1, slopeMap) * tree_counter(1, 2, slopeMap)


print(part_one(slopeMap))
print(part_two(slopeMap))

print(str(round(time.time() - start, 5)) + " seconds")

file.close()
