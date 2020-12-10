with open("jolts.txt", "r") as file:
    joltsList = [int(j.strip()) for j in file]

joltsList.append(0)
joltsList.append(max(joltsList) + 3)
joltsListSorted = sorted(joltsList)
threeCount = 0
oneCount = 0
for i in range(0, len(joltsListSorted) - 1):
    if joltsListSorted[i + 1] - joltsListSorted[i] == 3:
        threeCount += 1
    elif joltsListSorted[i + 1] - joltsListSorted[i] == 1:
        oneCount += 1
print(oneCount * threeCount)

calculatedList = {j: None for j in joltsListSorted}


def getCount(value):
    if value == max(joltsListSorted):
        return 1

    result = 0
    if value + 1 in joltsList:
        if calculatedList[value + 1] is not None:
            result += calculatedList[value + 1]
        else:
            resultToAdd = getCount(value + 1)
            calculatedList[value + 1] = resultToAdd
            result += resultToAdd
    if value + 2 in joltsList:
        if calculatedList[value + 2] is not None:
            result += calculatedList[value + 2]
        else:
            resultToAdd = getCount(value + 2)
            calculatedList[value + 2] = resultToAdd
            result += resultToAdd
    if value + 3 in joltsList:
        if calculatedList[value + 3] is not None:
            result += calculatedList[value + 3]
        else:
            resultToAdd = getCount(value + 3)
            calculatedList[value + 3] = resultToAdd
            result += resultToAdd
    return result


print(getCount(0))
