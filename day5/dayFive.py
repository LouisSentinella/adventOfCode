import math


def getPassID(bPass):
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7
    for item in bPass:
        if item == "L":
            max_col = ((min_col + max_col) // 2)
        elif item == "R":
            min_col = math.ceil((min_col + max_col) / 2)
        elif item == "F":
            max_row = ((min_row + max_row) // 2)
        elif item == "B":
            min_row = math.ceil((min_row + max_row) / 2)

    return min_row * 8 + min_col


with open("pass.txt", "r") as file:
    boardingPassList = [line.strip() for line in file]
2
idList = [getPassID(bPass) for bPass in boardingPassList]
print(max(idList))

idList.sort()
num = idList.pop(0)

for elem in idList:
    num += 1
    if elem != num:
        print(num)
        break
