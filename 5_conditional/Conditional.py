#conditional if/else - according a condition execute or not code

#Conditionals

#struct of conditional: take two values true or false according to case
#Note: Boolean data - can take two values TRUE or FALSE

#if condition is correct: True
#   then do this
#
#otherwise: False
#   do this

#Python comparison Operator
#   1. Equals - a == b
#   2. Not equals: a != b
#   3. less than: a < b
#   4. less than or equal to: a <= b
#   5. greater than: a > b
#   6. greater than or equal to: a >= b

#Python arithmetic operator

#   1. Addition x + y 
#   2. Subtraction x - y 
#   3. Multiplication x*y
#   4. Division x/y
#   5. Modulus x%y
#   6. Exponentiation x**y
#   7. Floor division x//y

#create a function for know if a number is greater than 10 
#recommend create function after call this

def greater(a):
    #convert string to number
    A = float(a) #float() convert string to float number
    print(A > 10) #return a value true or false
    print(type(A)) #type() - return data type
    if A > 10:
        return f"Number {A} is greater than 10"
    else:
        return f"Number {A} isn't greater than 10"

def give_numbers():
    number_1 = input(f"Number 1: ")
    Greater_10 = greater(number_1)
    print(Greater_10) #Greater_10 is variable local - scope

give_numbers()

#create a function for calculate the floor division between numbers
print("\n")

Number_3 = int(input("First number: ")) #other way convert string to number
Number_4 = int(input("Second number: "))

def floor_division(a, b):
    return a//b

Floor_value = floor_division(Number_3, Number_4)
print(f"Result:  {Floor_value}")
