n = 3
for i in range(1,n+1):
    print("*"*i)
for i in range(n): 
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))

for i in range(n):
    if i==0 or  i==n-1:
        print("* "*n)
    else:
        print("*" + (" ")*n +"*")
