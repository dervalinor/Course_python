#Dictionary is structure of data save different data

"""
Dictionary

1- Are used to store values in key:value pairs
2. Is a collection, which does not allow duplicate values

"""

user = { "name" : "Miguel", "age" : 23}

#show data type, this case is dictionary
print(type(user))

#show elements of the dictionary
print(user)

#access items in a dictionary by its key name

print("\n")
print(user["name"])
print(user["age"])

#ask data for save in dictionary

Book = input("Name of book: ")
Price = input("Price: ")

#save in a dictionary
buy_book = {"Libro":Book, "Precio":Price}
print(buy_book)
