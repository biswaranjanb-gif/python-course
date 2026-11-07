current_movies = {"JADDI(ODIA)": "10:00 AM", 
                  "DRISHYAM": "2:00 PM",
                  "HANUMAN ANSH": "6:00 PM"}

print('We are currently showing the following movies:')
for movie in current_movies:
    print(f"- {movie}")

movie = input("What movie would you like to watch? ")

showtime = current_movies.get(movie)

if showtime:
    print("The showtime for " + movie + " is " + showtime)
else:
    print("Sorry, we are not showing that movie.")



