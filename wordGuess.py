"""A word guessing game is a project that demonstrates the use of random selection, loops, conditional statements and string manipulation. In this game, the program randomly selects a word and the player must guess its characters within a limited number of attempts.


Word Guessing Game in Python :


The game begins by randomly choosing a word from a predefined list and hiding its characters. The player then guesses letters one at a time, with correct guesses revealing matching characters and incorrect guesses reducing the available attempts. The game ends when the word is fully revealed or all chances are exhausted.

Create a list of words and randomly select one.
Initialize variables to store guessed characters and remaining attempts.
Display the word using underscores for unguessed characters.
Accept a character from the user.
Check whether the character exists in the word.
Continue until the word is guessed or all attempts are exhausted.
Display the result."""

import random

name = input("Enter your name : ")
print("Good luck !", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)

print("Guess the character : ")
guesses = ''
turns = 12

while turns >0 :
 failed = 0
 for char in word:
  if char in guesses:
   print(char, end = " ")

  else :
   print("_", end =" ")
   failed += 1
 
 
 print()
 if failed == 0:
  print("You Win")
  print("The word is ", word)
  break

 guess = input("Enter a character : ").lower()

 if len(guess) != 1:
  print("Please enter a single character")
  continue
 if guess in guesses:
  print("This character is already guessed")
  continue
 guesses += guess

 if guess not in word:
  turns -= 1
  print("you have", turns, " more guesses")

  if(turns == 0):
   print("You Lose")
   print("The word was", word)
   