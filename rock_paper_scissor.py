import random
computer_choice = random.choice(["rock", "paper", "scissors"])
print("Computer chose: " + computer_choice)
user_choice = input("Enter your choice (rock, paper, scissors \n")
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
else:
    print("You lose!")