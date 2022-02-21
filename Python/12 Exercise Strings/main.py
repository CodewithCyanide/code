#Declaring variables with string data
greeting = "Good Morning, "
name = "Kapil"
print(type(name))
print("-"*50)
#Concatenating (Joining) two strings
c = greeting + name
print(c)
#Accessing a value from a string using the index
print(name[4])
# name[3] = "d" --> Does not work with strings
print("-"*50)
#Slicing strings using the slice operator [:]
print(name[1:4])
print("-"*50)
#String methods
print(len(name))
print("-"*50)
print("String".endswith("g"))
print("-"*50)
print("String".count("g"))
print("-"*50)
print("string".capitalize())
print("-"*50)
print("String".find("g"))
print("-"*50)
print("string".replace("g","f"))
print("-"*50)
#Using Escape characters (Sequence of characters after \)
print("A\nB") #It inserts a new line
print("-"*50)
print("A\tB") #It inserts a tab
print("-"*50)
print("\'")  #It inserts a singlequote
print("-"*50)
print("\\") #It inserts a backshash
print("-"*50)