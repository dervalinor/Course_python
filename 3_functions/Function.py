#function - section of code execute a action

#A function is defined using the def keyword

#create a function for make a multiply of two numbers

number_1= 3
number_2= 4

def multiply(a, b): #here we give the parameter
    #parameter can have a name different variables when define the function
    print(f"multiply of {a} and {b} is: {a*b}")

#now we must call the function for execute the code 
#Information can be passed into function as parameter
#Parameter are also called arguments

multiply(number_1, number_2) #give the parameter (name of variables)

#use of function: 
#   1- less code
#   2- reduce code duplication
#   3. more descriptive 

#create a function for give welcome user with his name

#Scope: A variable is only available from inside the region it is created

name = "Miguel" #Global scope: variables available from within any scope
welcome = "Welcome !!!"

def User_good_day(nombre, bienvenido):
    #local scope: variables created inside function, can only be 
    #used inside that function
    awesome= "Programming in python is awesome !!!"  
    #this variable only avable inside of function User_good_day 
    print(f"{name} {welcome}")
    print(awesome)

User_good_day(name, welcome)
