print("This program ouputs the sum of first n natural numbers")
num = int(input("Enter n: "))
sum = 0
for i in range(num+1):
    sum+=i
print(f"The sum of first {num} natural numbers is {sum}")