from copy import deepcopy

with open("instructions.txt", "r") as file:
    instructionsList = [[k.split()[0], k.split()[1], False] for k in file]


def runCode(accumulator, instructionsList):
    currentInstruction = instructionsList[0]
    instructionIndex = 0
    while not currentInstruction[2]:
        if currentInstruction[0] == "nop":
            instructionIndex += 1
            currentInstruction[2] = True
        elif currentInstruction[0] == "acc":
            accumulator += int(currentInstruction[1])
            currentInstruction[2] = True
            instructionIndex += 1
        elif currentInstruction[0] == "jmp":
            instructionIndex += int(currentInstruction[1])
            currentInstruction[2] = True

        if instructionIndex == len(instructionsList):
            return accumulator, True
        currentInstruction = instructionsList[instructionIndex]
    return accumulator, False


# Part One
print(runCode(0, deepcopy(instructionsList)))

# Part Two
for j in range(0, len(instructionsList)):
    if instructionsList[j][0] == "nop":
        instructionsToTest = deepcopy(instructionsList)
        instructionsToTest[j][0] = "jmp"
        accum, isFound = runCode(0, instructionsToTest)
        if isFound:
            print(accum)
            break
    elif instructionsList[j][0] == "jmp":
        instructionsToTest = deepcopy(instructionsList)
        instructionsToTest[j][0] = "nop"
        accum, isFound = runCode(0, instructionsToTest)
        if isFound:
            print(accum)
            break
