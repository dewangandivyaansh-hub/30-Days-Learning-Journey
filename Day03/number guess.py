#Number Guessing Game

import random
x=random.randint(1,101)
while True:
    guess=int(input(" \n Guess the number:"))
    if guess>x:
        print("\n You need to guess a lower number. \n")
    elif guess<x:
        print("\n You need to guess a higher number. \n")
    else:
        print("\n Correct guess, you won!!")
        break

    
