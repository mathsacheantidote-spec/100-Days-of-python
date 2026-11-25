"""Rock-Paper-Scissors is a game where player selects one of three options. Then the computer simultaneously makes a random selection. The program compares both choices using the game rules and declares the winner. The game can be played repeatedly until the user decides to quit.

Winning Rules
Rock defeats Scissors.
Scissors defeats Paper.
Paper defeats Rock.
If both players choose the same option, the round ends in a draw."""

import random

print("Welcome to Rock-Paper-Scissors!\n")
print("Winning Rules:")
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins\n")

choices = ["Rock", "Paper", "Scissors"]

while True:
    print("Choose an option: ")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    try :
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a valid number")
        continue

    while choice < 1 or choice > 3:
        choice = int(input("Enter a valid choice (1-3): "))

    user_choice = choices[choice-1]

    print("User choice is : ", user_choice)
    print("Now it's computer turn...")

    comp_choice = random.randint(1,3)
    computer_choice = choices[comp_choice-1]

    print("computer choice is ", computer_choice)
    print(user_choice, "vs" , computer_choice)


    if choice == comp_choice:
        print("It's a tie....")

    elif (
        (choice == 1 and choice == 3) or
        (choice == 2 and choice == 1) or
        (choice == 3 and choice == 1)
    ):
        print("You Win! Congratulations.")

    else : 
        print("Computer Wins")

    while True:
        ans = input("Do you want to play again? (Y/N)\n").lower()

        if ans in ['y' , 'n']:
            break
        
        print("Please enter Y or N.")

    if ans == 'n':
        break

    print()

print("\nThanks for playing!")
