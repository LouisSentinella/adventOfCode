with open("numbers.txt", "r") as file:
    numbersList = [int(j.strip()) for j in file]


def isSumOfLast25(numbersList, index):
    last25 = numbersList[index - 25:index]
    for i in last25:
        for j in last25:
            if i + j == numbersList[index]:
                return True
    else:
        return False


for i in range(25, len(numbersList)):
    if not isSumOfLast25(numbersList, i):
        encryptionWeakness = numbersList[i]
        break
print(encryptionWeakness)

found = False
for i in range(0, len(numbersList)):
    sumList = [numbersList[i]]
    for j in range(i + 1, len(numbersList)):
        if sum(sumList) == encryptionWeakness:
            found = True
            break
        elif sum(sumList) > encryptionWeakness:
            break
        else:
            sumList.append(numbersList[j])
    if found:
        print(min(sumList) + max(sumList))
        break
