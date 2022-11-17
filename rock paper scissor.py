import random

print("Welcome to Rock, Paper and Scissor game \nYou have 5 chances to play.")

lifes = 0
your_points = 0
comp_points = 0
draw = 0

while (lifes < 5):

    options = ["Rock", "Paper", "Scissor"]
    comp = random.choice(options)

    user = input("\nWhat would you like to choose\nPress R for rock, P for paper and S for scissors\nYour Input:")

    if user == "r" and comp == "Scissor":
        print(f"You choose: {user} and Computer choose: {comp}, You won")
        your_points = your_points + 1
        comp_points = comp_points + 0

        if user == "r" and comp == "Paper":
            print(f"You choose: {user} and Computer choose: {comp}, You lost")
            your_points = your_points + 0
            comp_points = comp_points + 1

    elif user == "p" and comp == "Rock":
        print(f"You choose: {user} and Computer choose: {comp}, you won")
        your_points = your_points + 1
        comp_points = comp_points + 0

        if user == "p" and comp == "Scissor":
            print(f"You choose: {user} and Computer choose: {comp}, you lost")
            your_points = your_points + 0
            comp_points = comp_points + 1

    elif user == "s" and comp == "Paper":
        print(f"You choose: {user} and Computer choose: {comp}, You won")
        your_points = your_points + 1
        comp_points = comp_points + 0

        if user == "s" and comp == "Rock":
            print(f"You choose: {user} and Computer choose: {comp}, you lost")
            your_points = your_points + 0
            comp_points = comp_points + 1


    elif user == "s" and comp == "Scissor" or user == "r" and comp == "Rock" or user == "p" and comp == "Paper":
        print(f"You choose: {user} and Computer choose: {comp}, It's a draw")
        your_points = your_points + 0
        comp_points = comp_points + 0
        draw = draw + 1

    else:
        print(f"Invalid Input: Please enter correct input")

    lifes += 1

print("All lives ended")
print(f"You win: {your_points} times")
print(f"Computer win: {your_points} times")
print(f"Match tied: {draw} times")
