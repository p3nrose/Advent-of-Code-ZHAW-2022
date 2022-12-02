# A for Rock, B for Paper, C for Scissors
# X for Rock, Y for Paper, Z for Scissors

# 1 Point for Rock, 2 Points for Paper, 3 Points for Scissors
# 0 Points for Loss, 3 Point for Tie, 6 Points for Win


score = 0
# read the input file in /input/2.in
f = open('input/2.in', 'r')
# while there is still a line to read calculate the score


lines = f.readlines()

for line in lines:
    # split the line into the two players moves
    clean_line= line.strip('\n')
    moves = clean_line.split(' ')
    # # calculate score for player 2
    # # tie
    if moves[0] == 'A' and moves[1] == 'X':
        score = score + 1 + 3
    # # win
    elif moves[0] == 'A' and moves[1] == 'Y':
        score = score + 2 + 6
    # # loss
    elif moves[0] == 'A' and moves[1] == 'Z':
        score = score + 3 + 0
    # # loss
    elif moves[0] == 'B' and moves[1] == 'X':
        score = score + 1 + 0
    # # tie
    elif moves[0] == 'B' and moves[1] == 'Y':
        score = score + 2 + 3
    # # win
    elif moves[0] == 'B' and moves[1] == 'Z':
        score = score + 3 + 6
    # # win
    elif moves[0] == 'C' and moves[1] == 'X':
        score = score + 1 + 6
    # # loss
    elif moves[0] == 'C' and moves[1] == 'Y':
        score = score + 2 + 0
    # # tie
    elif moves[0] == 'C' and moves[1] == 'Z':
        score = score + 3 + 3
#
print(score)
