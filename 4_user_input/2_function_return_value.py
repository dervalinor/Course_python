#a fubction can return a value
#A function can return data as a result

#create a function return a number

#step function return value

#1. function is executed
def number():
    a = input("Number: ")
    return a
#2. return value is assigned to variable
b = number() #call the function for can see the value
print(f"Number is: {b}")#3. variable value is print

#input() - always returns a string

#create a function return the sum of two numbers

number_1 = input("\nNumber 1: ")#as print return string we must convert a number
number_2 = input("Number 2: ")


def sum_two(a, b): #here declare a and b for function
    #convert a number integer
    A = int(a)
    B = int(b)
    return A + B

sum_number = sum_two(number_1, number_2)
print(f"\nsum: {sum_number}")
