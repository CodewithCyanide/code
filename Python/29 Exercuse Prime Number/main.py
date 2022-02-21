print("This program tells whether a given number is prime or not.")
number = int(input("Enter a number to check: "))
isPrime=True
for i in range(2,number):
    if number%i==0: #If number is divisible by any number, then it is not prime
        isPrime=False
if isPrime:
    print("This number is a Prime Number")
else:
    print("This number is not a Prime Number")