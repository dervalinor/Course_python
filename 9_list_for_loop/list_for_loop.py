#remember data types so far: string, integer, float and boolean (True or False)

#list: To store multiple items in a single variable and can contain
#different data types, as list of numbers, list string ...
list_element = [True, 4, "sometext"]

#show element of next list
list_numbers = [1, 2, 3, 4]

#for loop: Is used iterating over a sequence (like a list)
#Now we goint to show the element of the list_numbers

print("Element of the list: \n")
for number in list_numbers: 
    print(f"{number}")
print("\n")

#we can convert a string to list with split()

#Default separator is any whitespace, this reason
#we must give the separator of element as parameter in split()

list_num = "12,23,45" #convert string to list

def string_list(list_num):
    for num in list_num.split(","): #indicate separator is comma
        print(f"{num} ")

Result = string_list(list_num)

print("\n")

#comments several lines
"""Basic list operations

1- create a list 
2- add an item to the list
3- remove an item from the list
4- change items in the list 
5- access items of the list """

my_list = ["book", "stocks", "analysis", "time"]

#access item of the list
#Now we going to access to element in the position zero

element_zero = my_list[0] #first element of the list
print(f"first element of the list: {element_zero}")

#second element of the list
print(f"second element of the list: {my_list[2]}")

#add element to the list
my_list.append("think")
print(f"New element to the list: {my_list}")
