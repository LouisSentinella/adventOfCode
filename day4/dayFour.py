import time

start = time.time()

file = open("passportsJphn.txt", "r")


def isValidOne(passportRowList):
    requiredVars = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for k in requiredVars:
        if not any(k in sublist for sublist in passportRowList):
            return False

    return True


def isValidTwo(passportRowList):
    if not isValidOne(passportRowList):
        return False

    byr = next(subl for subl in passportRowList if 'byr' in subl)[1]
    if len(byr) == 4:
        if not (1920 <= int(byr) <= 2002):
            return False
    else:
        return False

    iyr = next(subl for subl in passportRowList if 'iyr' in subl)[1]
    if len(iyr) == 4:
        if not (2010 <= int(iyr) <= 2020):
            return False
    else:
        return False

    eyr = next(subl for subl in passportRowList if 'eyr' in subl)[1]
    if len(eyr) == 4:
        if not (2020 <= int(eyr) <= 2030):
            return False
    else:
        return False

    hgt = next(subl for subl in passportRowList if 'hgt' in subl)[1]
    if (hgt.endswith('cm')):
        if not 150 <= int(hgt.removesuffix('cm')) <= 193:
            return False
    elif hgt.endswith('in'):
        if not 59 <= int(hgt.removesuffix('in')) <= 76:
            return False
    else:
        return False

    hcl = next(subl for subl in passportRowList if 'hcl' in subl)[1]
    if hcl[0] == '#':
        for i in hcl.removeprefix('#'):
            if i not in "abcdef0123456789":
                return False
    else:
        return False

    ecl = next(subl for subl in passportRowList if 'ecl' in subl)[1]
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    pid = next(subl for subl in passportRowList if 'pid' in subl)[1]
    if len(pid) == 9:
        try:
            int(pid)
        except:
            return False
    else:
        return False

    return True


passportList = []
passportRow = []
for line in file:
    if line != '\n':
        for j in line.strip().split():
            passportRow.append(j.split(':'))
    else:
        passportList.append(passportRow)
        passportRow = []
passportList.append(passportRow)


def partOne(passportList):
    counter = 0
    for i in passportList:
        if isValidOne(i):
            counter += 1

    print(counter)


def partTwo(passportList):
    counter = 0
    for i in passportList:
        if isValidTwo(i):
            counter += 1

    print(counter)


partOne(passportList)
partTwo(passportList)

print(str(round(time.time() - start, 8)) + " seconds")

file.close()
