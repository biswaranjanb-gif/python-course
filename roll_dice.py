import random
comp_choice = random.randint(1,6)
print ("Computer rolled: " + str(comp_choice))

user_choice = int(input("Enter your choice (1-6):"))
print("You rolled: " + str(user_choice))

if user_choice == comp_choice:
    print("It's a tie!")
elif user_choice > comp_choice:
    print("You win!")
elif user_choice < comp_choice:
    print("You lose!")
else:
    print("Invalid input. Please enter a number between 1 and 6.")      
    