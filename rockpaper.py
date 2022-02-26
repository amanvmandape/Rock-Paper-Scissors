import random
import os
import time

p1_wins = 0
p2_wins = 0

def winner():
    global moves
    global p1_wins
    global p2_wins
    p1_win = p1 == "R" and p2 == "S" or p1 == "S" and p2 == "P" or p1 == "P" and p2 == "R"
    p2_win = p2 == "R" and p1 == "S" or p2 == "S" and p1 == "P" or p2 == "P" and p1 == "R"
    
    if p1_win == p2_win:
        print("This Round is Draw")
        time.sleep(2)
    elif p1_win:
        p1_wins = p1_wins + 1
        print("You won this Round")
        time.sleep(2)
    elif p2_win:
        p2_wins = p2_wins + 1
        print("You lost this Round")
        time.sleep(2)
    
    os.system('cls')
    print("Welcome to Rock Paper Scissors")
    print("Enter R for Rock, P for Paper, S for Scissors")
    print("You: ",p1_wins,"\t PC: ",p2_wins)


print("Welcome to Rock Paper Scissors")
print("Enter R for Rock, P for Paper, S for Scissors")

while(p1_wins<3 and p2_wins<3):
    p1 = input("Enter your choice: ")

    p2 = random.choice(["R","P","S"])

    winner()

if p1_wins>p2_wins:
    print("You have Won")
else:
    print("You Lost")