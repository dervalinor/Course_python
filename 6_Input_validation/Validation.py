#validation evoid error to user give a data different to necessary
#Example: user give a text for calculate math

#create a program for validation of number (the user must give a number and 
#show error if give a text)

number = input("Number: ");

if number.isdigit(): #if variable is integer number then true
    print("This variable is a number")
else:
    print("This variable isn't number")
