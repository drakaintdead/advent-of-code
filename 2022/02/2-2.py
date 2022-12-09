input = open("input.txt", "r")
inputData = input.read().splitlines()
# A/X = Rock = 1
# B/Y = Paper = 2
# C/Z = Scissors = 3

First = lambda num: inputData[num][0]
Second = lambda num: inputData[num][2]

score = 0

for i in range(len(inputData)):
    opponent = First(i)
    outcome = Second(i)
    if outcome == "X":
        if opponent == "A":
            # i am scissors
            score += 3
        elif opponent == "B":
            # i am rock
            score += 1
        elif opponent == "C":
            # i am paper
            score += 2
    elif outcome == "Y":
        if opponent == "A":
            # i am rock
            score += 4
        elif opponent == "B":
            # i am paper
            score += 5
        elif opponent == "C":
            # i am scissors
            score += 6
    elif outcome == "Z":
        if opponent == "A":
            # i am paper
            score += 8
        elif opponent == "B":
            # i am scissors
            score += 9
        elif opponent == "C":
            # i am rock
            score += 7

print(score)