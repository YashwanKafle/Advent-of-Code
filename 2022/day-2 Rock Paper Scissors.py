with open("day2.in") as file:
    data = [i for i in file.read().strip().split('\n')]

score = 0 

win = 6
draw = 3
lose = 0

rock = 1
paper = 2
scissors = 3

'''PART 1'''
for game in data:
    opponent,player = game.split(' ')   
    '''
    A,X - Rock
    B,Y - Paper
    C,Z - Scissors
    '''
    if opponent == "A":
        if player == "X":
            score +=draw + rock
        if player == "Y":
            score +=win + paper
        if player == "Z":
            score +=lose + scissors
    if opponent == "B":
        if player == "X":
            score +=lose + rock
        if player == "Y":
            score +=draw + paper
        if player == "Z":
            score +=win + scissors
    if opponent == "C":
        if player == "X":
            score +=win + rock
        if player == "Y":
            score +=lose + paper
        if player == "Z":
            score +=draw + scissors

print(score)

'''Part 2'''
for game in data:
    opponent,player = game.split(' ')   
    '''
    A,X - Rock
    B,Y - Paper
    C,Z - Scissors
    '''
    if opponent == "A":
        if player == "Y":
            score +=draw + rock
        if player == "Z":
            score +=win + paper
        if player == "X":
            score +=lose + scissors
    if opponent == "B":
        if player == "X":
            score +=lose + rock
        if player == "Y":
            score +=draw + paper
        if player == "Z":
            score +=win + scissors
    if opponent == "C":
        if player == "Z":
            score +=win + rock
        if player == "X":
            score +=lose + paper
        if player == "Y":
            score +=draw + scissors

print(score)