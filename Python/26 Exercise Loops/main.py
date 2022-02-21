#Using while loop with a start variable
i = 0
while i<10:
    print("Yes " + str(i))
    i = i + 1

print("Done")
print("-"*50)
#Using while loop with a list 
fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']
i = 0
while i<len(fruits):
    print(fruits[i])
    i = i+1
print("Done")
print("-"*50)
#Using for loop with a list
fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']

for item in fruits:
    print(item)
print("Done")
print("-"*50)
#Using for loop with range(start, end, step)
for i in range(1, 8, 1):
    print(i)
print("Done")
print("-"*50)
#Using for loop with else
for i in range(10):
    print(i)
else:
    print("This is inside else of for")
print("Done")
print("-"*50)
#Using break with for loop 
for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("This is inside else of for")
print("Done")
print("-"*50)
#Using continue with for loop
for i in range(10):
    if i == 5:
        continue
    print(i)
print("Done")
print("-"*50)
#Using pass with loops
# while i>6:
#   pass
print("Done")
print("-"*50)