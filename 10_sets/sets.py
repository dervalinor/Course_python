"""
Set: ordered a list and search no repeat element

- another built-in data type of python
- as with lists, used to store multiple items of data
- does NOT allow duplicate values

"""

list_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Friday"]

#repeat two time Friday
print(f"list of day: {list_of_days}")

#set friday repeat only one time
set_of_days = set(list_of_days) #transform list to set
#input: the user input array
#output: Returns the converted set

print(f"Set of days: {set_of_days}")

#other way of make this is:
print(set(list_of_days))
print("\n")

#declare a set
set_of_numbers = {1, 2, 3}
print(set_of_numbers)

"""
Basic set operations

1. Create a set
2. Access items only via loop
3. Add an item to the set
4. Remove an item from the set

Unordered and unchangeable

1. Items in a set do not have a defined order!
2. Items cannot be refered to by index!
3. Items cannot be changed, only added/removed!

"""

#access to items of the set
print("Item of the set: ")
for items in set_of_numbers:
    print(items)

print("\n")
#add element to set
set_of_numbers.add(4)
for items in set_of_numbers:
    print(items)

print("\n")
#remove element
set_of_numbers.remove(3) #delete the number 3 of the set
for items in set_of_numbers:
    print(items)
