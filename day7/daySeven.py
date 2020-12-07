import time

start = time.time()

with open("bags.txt", "r") as file:
    dataStructure = {(k.strip().split()[0] + k.strip().split()[1]): ([j.strip().replace(",", "").replace(".", "") for j in k.strip().split()[4::]]) for k in file}


def is_gold_deep(name):
    for j in [i + 1 for i in range(0, len(dataStructure[name])) if i % 4 == 0]:
        if (dataStructure[name][j] + dataStructure[name][j + 1]) == "shinygold":
            return True
        elif dataStructure[name][j] + dataStructure[name][j + 1] == "otherbags":
            return False
    else:
        for j in [i + 1 for i in range(0, len(dataStructure[name])) if i % 4 == 0]:
            if is_gold_deep(dataStructure[name][j] + dataStructure[name][j + 1]):
                return True
        else:
            return False


print(sum([is_gold_deep(bag_rule) for bag_rule in dataStructure]))


def find_those_bad_boys(name):
    count = 0
    if dataStructure[name][1] + dataStructure[name][2] == "otherbags":
        return 0
    for j in [i + 1 for i in range(0, len(dataStructure[name])) if i % 4 == 0]:
        deeper_count = find_those_bad_boys(dataStructure[name][j] + dataStructure[name][j + 1])
        if deeper_count == 0:
            count += int(dataStructure[name][j - 1])
        else:
            count += int(dataStructure[name][j - 1])
            count += deeper_count * int(dataStructure[name][j - 1])
    return count


print(find_those_bad_boys("shinygold"))

print(str(round(time.time() - start, 8)) + " seconds")