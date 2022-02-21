#Creating a dictionary using {} 
details = {
    "name":"Kapil",
    "age":"18",
    "height":6.2,
    "drunk": False,
    "girlfriend":None
}
#Accessing value of name 
print(details["name"])
print("-"*50)
#Getting dictionary in form of a list of key value pairs
print(details.items())
print("-"*50)
#Getting hold of all the keys 
print(details.keys()) # => we can typecast it into list
print("-"*50)
#Updating dictionary 
details.update({"friend":"Joe"})
print(details)
print("-"*50)
#Getting hold of a value and avoiding error if key is not found
print(details.get("friend"))
print("-"*50)

# An empty set can be created using the below syntax:
b = set()
print(type(b))

## Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set
b.add((4, 5, 6))

## Accessing Elements
# b.add({4:5}) # Cannot add list or dictionary to sets
print(b)

## Length of the Set
print(len(b)) # Prints the length of this set

## Removal of an Item
b.remove(5) # Removes 5 fromt set b
# b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(b)

print(b.pop())
print(b)