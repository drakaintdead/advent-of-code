input = open("input.txt", "r")
inputData = input.read().splitlines()
# A/X = Rock
# B/Y = Paper
# C/Z = Scissors

First = lambda num: inputData[num][0]
Second = lambda num: inputData[num][2]

score = 0

for i in range(len(inputData)):
    opponent = First(i)
    player = Second(i)
    if player == "X":
        score += 1
        if opponent == "C":
            score += 6
        elif opponent == "A":
            score += 3
    elif player == "Y":
        score += 2
        if opponent == "A":
            score += 6
        elif opponent == "B":
            score += 3
    elif player == "Z":
        score += 3
        if opponent == "B":
            score += 6
        elif opponent == "C":
            score += 3
print(score)

