# function to roll a dice
import random

def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total_score = dice1 + dice2
    return total_score

def main():
    player1 = input("Enter player1 name: ")
    player2 = input("Enter player2 name: ")

    player1_score = roll_dice()
    player2_score = roll_dice()

    print(player1 + " rolled: " + str(player1_score))
    print(player2 + " rolled: " + str(player2_score))

    if player1_score > player2_score:
        print(player1 + " wins!")
    elif player1_score < player2_score:
        print(player2 + " wins!")  
    elif player1_score == player2_score:    
        print("It's a tie!")

main()