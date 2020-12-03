# Creating game rock,Paper,Scissor

import random
l = ['R','P','S']
computer_turn = random.choice(l)
point,loose = 0,0
another_round = 'Y'
while another_round == 'Y':
    print("Choose: Rock[R],Paper[P],Scissor[S] \n Shoot_")
    choose = input("R, P, S :  ")
    if choose.upper() == 'R' and (computer_turn == 'P' or computer_turn == 'S'):
        print("You gain POINT")
        point += 1
    elif choose.upper() == 'S' and computer_turn == 'P':
        print("You gain POINT")
        point += 1
    elif choose == computer_turn:
        print("Both users select same choice")
        continue
    else:
        print("No Point")
        loose += 1

    another_round = input("Want another round(Y/N):  ").upper()
print(f"Total rounds: {point+loose}")
print(f"Number of times you win: {point}")
print(f"Number of times computer wins: {loose}")
if point > loose:
    print("WINNER")
elif point == loose:
    print("NO ONE WINS")
else:
    print("YOU LOOSE")

