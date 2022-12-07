from itertools import groupby

input = open("input.txt", 'r')
inputData = input.read().splitlines()
splitData = [list(g) for k,g in groupby(inputData, key=lambda s: s!="") if k]
for i in range(0, len(splitData)):
    for x in range(0, len(splitData[i])):
        splitData[i][x] = int(splitData[i][x])

biggestNumber = 0

for i in range(len(splitData)):
    if sum(splitData[i]) > biggestNumber:
        biggestNumber = sum(splitData[i])
    
print(f"Largest amount being carried by 1 elf: {biggestNumber} calories")
