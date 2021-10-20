#handle: manejo

#try and except
#The try block: lets you "test" a block of code for errors.
#The except block: catches the error and lets you handle it.

#create a function for validation a integer number

number = input("Number: " ) #try if this variable is a number

def validation(a):
    try:
        A = int(a) #if this function mark error then show "except ValueError"
        print("This variable is a number")

    except ValueError:
        print("This variable isn't a number")

validation(number)#remember call function

#try/except is similar to if/else but for errors
