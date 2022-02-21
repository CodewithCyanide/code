print("This program generates the name of your band!")
#1. Create a greeting for your program.
print("Welcome to Band Name Generator!")
#2. Ask the user for the city that they grew up in.
cityName = input("In which city you grew up in?\n")
#3. Ask the user for the name of a pet.
petName = input("What is the name of your pet?\n")
#4. Combine the name of their city and pet and show them their band name.
bandName = cityName.title() +"'s" + " " + petName.title()
#5. Output the final result with a f string
print(f"Your Band Name could be {bandName}")