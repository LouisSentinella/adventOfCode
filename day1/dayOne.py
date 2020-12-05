import time

start = time.time()

file = open("numbers.txt", "r")

numbersList = [int(i.strip()) for i in file]


def twoLines(numbersList):
    print(next(i * j for i in numbersList for j in numbersList if i + j == 2020))
    print(next(i * j * k for i in numbersList for j in numbersList for k in numbersList if i + j + k == 2020))


def partOne(numbersList):
    # return ([i * j for i in numbersList for j in numbersList if i + j == 2020][0])
    for i in numbersList:
        for j in numbersList:
            if i + j == 2020:
                return i * j


def partTwo(numbersList):
    # return ([i * j * k for i in numbersList for j in numbersList for k in numbersList if i + j + k == 2020][0])
    for i in numbersList:
        for j in numbersList:
            for k in numbersList:
                if i + j + k == 2020:
                    return i * j * k


print(partOne(numbersList))
print(partTwo(numbersList))

#twoLines(numbersList)

print(str(round(time.time() - start, 5)) + " seconds")

file.close()
