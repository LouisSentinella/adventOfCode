import itertools
import time

start = time.time()


answerList = []
answerRow = []
count = 0

with open("answers.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line != '':
            answerRow.append(line)
        else:
            answerList.append(answerRow)
            count += len([k for k, g in itertools.groupby(sorted(itertools.chain.from_iterable(answerRow)))])
            answerRow = []

print(count)

count = 0

for row in answerList:
    intersect = row[0]
    for index, answer in enumerate(row):
        set1 = set(answer)
        intersect = list(set1.intersection(intersect))
    count += len(intersect)

print(count)

print(str(round(time.time() - start, 8)) + " seconds")
