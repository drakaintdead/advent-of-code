input = open("input.txt", "r")
inputData = input.read().splitlines()

splitList = []

count = 0
count2 = -1

for i in inputData:
    count += 1
    count2 += 1
    if count == 3:
        count = 0

        splitList.append([inputData[count2], inputData[count2-1], inputData[count2-2]])

print(splitList)

score = 0

for i in splitList:
    set1 = set(i[0])
    set2 = set(i[1])
    set3 = set(i[2])
    commonChar = set1.intersection(set2, set3)
    for x in commonChar:
        commonChar = x
    asciiValue = ord(commonChar)
    if asciiValue > 90:
        score += asciiValue - 96
    else:
        score += asciiValue - 38

print(score)