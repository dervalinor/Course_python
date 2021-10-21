#looping

# To execute logic multiple times
# python has 2 loop commands
# similar to if statements, a loops evaluate to true or false
# a loop is executing while the condition is true

#create a function where user could say when want exit this

option = "No"

while option == "No" or option == "no" or option == "NO":
    #if is true execute code

    #logic operator: and (must are all options true) - or (only option true)
    option = input("do you sure of exit?: ")
    print("\n")
