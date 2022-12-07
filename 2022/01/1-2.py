from itertools import groupby

input = open("input.txt", 'r')
inputData = input.read().splitlines()
splitData = [list(g) for k,g in groupby(inputData, key=lambda s: s!="") if k]
print(splitData)
for i in range(0, len(splitData)):
    for x in range(0, len(splitData[i])):
        splitData[i][x] = int(splitData[i][x])

print(splitData)

addedList = []

for i in range(len(splitData)):
    addedList.append(sum(splitData[i]))
    
topThree = sorted(addedList, reverse=True)[:3]
print("Sum of top 3: " + str(sum(topThree)))