# Virtual dice game, you win if you roll six, you lose one life if not
#You have three lives
from random import randint

lives = 3
while True:
    dice_roll = randint(1, 6)
    if dice_roll == 6:
        print("Congrats! You rolled a 6. You Win!")
        break
    else:
        lives = lives-1 #you lose a life, if this line is ommited the game will go on until we roll a 6, always winning at the end
        print(f"You rolled a {dice_roll}. You lose a life, lives left {lives}")
        if lives == 0:
            print("You didn't roll a 6. You lose!")
            break
print("Thanks for playing my game")

