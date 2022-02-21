print("This program takes a year and tells whether it is a leap year or not")
year = int(input("Which year do you want to check? "))
if year%4==0: #If year is divisible by 4, it is a leap year
  if year%100==0: #If year is divisible by 100, it is not a leap year
    if year%400==0: #If year is divisible by 400, it is a leap year
      print("leap year")
    else:
      print("Not a leap year.")
  else:
    print("leap year")
else:
  print("Not leap year.")