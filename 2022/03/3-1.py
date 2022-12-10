input = open("input.txt", "r")
inputData = input.read().splitlines()

splitList = []

for i in inputData:
    firstPart, secondPart = i[:len(i)//2], i[len(i)//2:]
    splitList.append([firstPart, secondPart])


score = 0

for i in splitList:
    set1 = set(i[0])
    set2 = set(i[1])
    commonChar = set1 & set2
    for x in commonChar:
        commonChar = x
    asciiValue = ord(commonChar)
    if asciiValue > 90:
        score += asciiValue - 96
    else:
        score += asciiValue - 38

print(score)