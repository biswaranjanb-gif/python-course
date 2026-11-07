expenses = [100,200,300,400,500,600]

sum = 0
for expense in expenses:
    sum+= expense

print("You spent $" + str(sum)) 

total=0
expenses = []
for i in range(7):
    expenses.append(int(input("Enter an expense:")))
    total+=expenses[i]
    print(i)

print("You spent $" + str(total))
print(expenses)