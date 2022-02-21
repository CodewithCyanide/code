print("This program takes a two digit number and sums up both digits of it.")
#Asking for a two digit number
two_digit_number = input("Type a two digit number: ")
#Here the type of two_digit_number is string
#Using subscript to extract digits and type casting them
firstDigit = int(two_digit_number[0])
secondDigit = int(two_digit_number[1])
#Adding both
sum = firstDigit+secondDigit
#Outputting result
print(f"The sum of both of its digits is {sum}")
