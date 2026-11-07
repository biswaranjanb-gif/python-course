temperature = float(input("Enter the temperature in Fahrenheit: "))
weather = input("Enter the weather condition (sunny, rainy, cloudy): ").lower()

if temperature > 80:
    print("It's too hot!")
    print("Stay inside")
else:
    print("Enjoy the weather!")
print("Have a nice day!")

if weather == "sunny":
    print("It's sunny today.")
elif weather == "rainy":
    print("It's rainy today.")
elif weather == "cloudy"                    :
    print("It's cloudy today.")
elif not weather == "sunny" and not weather == "rainy" and not weather == "cloudy":
    print("Weather condition unknown.")