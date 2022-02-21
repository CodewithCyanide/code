print("This program gives the factorial of the given number.")
number = int(input("Please Enter a number:\n"))
temp=number
for i in range(1, number):
    temp*=i
print(f"The factorial of {number} is {temp}.")



