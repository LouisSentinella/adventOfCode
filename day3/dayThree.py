import time

start = time.time()

file = open("slope.txt", "r")

slopeMap = [[location for location in line.strip()] for line in file]

def tree_counter(xInc, yInc, slopeMap):
    x, y = 0,0
    treeCounter = 0
    while y < len(slopeMap) - 1:
        x, y = (x + xInc) % len(slopeMap[0]), y + yInc
        if slopeMap[y][x] == '#':
            treeCounter += 1
    return treeCounter


def part_one(slopeMap):
    return tree_counter(3, 1, slopeMap)


def part_two(slopeMap):
    return tree_counter(1, 1, slopeMap) * tree_counter(3, 1, slopeMap) * tree_counter(5, 1, slopeMap) * tree_counter(7, 1, slopeMap) * tree_counter(1, 2, slopeMap)


print(part_one(slopeMap))
print(part_two(slopeMap))

print(str(round(time.time() - start, 8)) + " seconds")

file.close()
