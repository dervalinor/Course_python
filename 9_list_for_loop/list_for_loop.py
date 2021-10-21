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
