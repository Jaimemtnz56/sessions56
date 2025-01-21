# Virtual dice game (using while function), you win if you roll six, you lose one life if not
#You have three lives
from random import randint

lives = 3
while lives > 0:
    dice_roll = randint(1, 6)
    if dice_roll == 6:
        print("Congrats! You rolled a 6. You Win!")
        break
    else:
        lives = lives-1 #you lose a life
        print(f"You rolled a {dice_roll}. You lose a life, lives left {lives}")
else:
    print("You didn't roll a 6. You lose!")

