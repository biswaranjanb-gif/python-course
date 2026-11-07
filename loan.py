# Get details of loan
money_owed = float(input("Enter the amount of money owed : ")) #50,000
apr = float(input("Enter the annual percentage rate (APR) : ")) # 3%
payment = float(input("Enter the monthly payment : ")) # 1,000
months = int(input("Enter the number of months : ")) # 24

monthly_interest_rate = apr / 100 / 12

for i in range (months):
    # Calculate interest to pay
    interest_paid = money_owed * monthly_interest_rate

    # Add in Interest
    money_owed = money_owed + interest_paid

    if (money_owed - payment) < 0:
        print("Tha last payment is", money_owed)
        print('You paid off the loan in', i + 1, 'months.')
        break

    # make payment
    money_owed = money_owed - payment
    print('Paid', payment, 'of which', interest_paid, 'was interest. You now owe', money_owed)


 


                         