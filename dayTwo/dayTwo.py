import time

start = time.time()

file = open("passwords.txt", "r")
passwordsList = []
for i in file:
    i = i.strip('\n')
    i = i.split()
    i[0] = i[0].split('-')
    i[1] = i[1].strip(':')
    passwordsList.append(i)


def partOne(passwordsList):
    correctCounter = 0
    for i in passwordsList:
        counter = 0
        for letter in i[2]:
            if letter == i[1]:
                counter += 1
        if int(i[0][0]) <= counter <= int(i[0][1]):
            correctCounter += 1
    return correctCounter


def partTwo(passwordsList):
    correctCounter = 0
    for i in passwordsList:
        if i[2][int(i[0][0]) - 1] == i[1]:
            if i[2][int(i[0][1]) - 1] != i[1]:
                correctCounter += 1
        elif i[2][int(i[0][1]) - 1] == i[1]:
            if i[2][int(i[0][0]) - 1] != i[1]:
                correctCounter += 1
    return correctCounter


print(partOne(passwordsList))
print(partTwo(passwordsList))

print(str(round(time.time() - start, 5)) + " seconds")
