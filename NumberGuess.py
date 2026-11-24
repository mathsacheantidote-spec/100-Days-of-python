"""Number Guessing Game is a game in which the computer randomly selects a number between 1 and 100. The user must guess the number within a limited number of attempts. After each incorrect guess, the program provides a hint indicating whether the guess is too low or too high.




Winning Rules:

Computer generates a random number between 1 and 100.
User has a maximum of 7 attempts to guess the number.
User wins immediately if the guess matches the randomly generated number.
If the guess is lower than the selected number, the program displays "Too Low" and the user should try a higher number.
If the guess is higher than the selected number, the program displays "Too High" and the user should try a lower number.
Invalid input or numbers outside the range of 1 to 100 do not count as an attempt.
If the user does not guess the number within 7 valid attempts, the game ends and reveals the correct number.
"""









import random

attempts = 7

def display_rules():
    print("Welcome to Number Guessing Game.\n")
    print("I have selected a number between 1 to 100.")
    print("You have 7 attempts to guess it !\n")

def play_game(number , attempt =1):
    if(attempt > attempts):
        print("Game Over!\n")
        print("The correct number was: ", number)
        return
    guess  = input(f"Attempt : {attempt} of 7 - Enter your guess : ")

    try:
     guess = int(guess)

    except ValueError:
     print("Please enter a valid integer input b/w given limits")
     return play_game(number , attempt)

    if guess < 1 or guess > 100:
       print("Please enter a valid number between 1 to 100")
       return play_game(number , attempt)

    
    check_guess = lambda x, y : "correct" if x == y else ("low" if x < y else "high")
    result = check_guess(guess , number)

    if result == "correct":
       print("Congratulations!\n You guessed it right")
       print("You guessed it in" , attempt, "attempt(s)")
       return 

    if result == "low":
       print("try a higher number!")

    if result == "high":
       print("try a lower number!")

    play_game(number , attempt+1)

display_rules()

random_num = random.randint(1,100)
play_game(random_num)