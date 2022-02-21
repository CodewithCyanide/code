print("This program takes a number and prints multplication table of it")
number = int(input("Please enter a number to get multiplication table"))
for i in range(0,11):
    print(f"{number} x {i} = {number*i}")