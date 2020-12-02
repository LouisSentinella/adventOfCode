file = open("numbers.txt", "r")
numbersList = []
for i in file:
    numbersList.append(i.strip('\n'))

def partOne(numbersList):
    for i in numbersList:
        for j in numbersList:
            if int(i) + int(j)  == 2020:
                return(int(i)*int(j) )

def partTwo(numbersList):
    for i in numbersList:
        for j in numbersList:
            for k in numbersList:
                if int(i) + int(j) +int(k) == 2020:
                    return (int(i)*int(j) * int(k))




print(partOne(numbersList))
print(partTwo(numbersList))