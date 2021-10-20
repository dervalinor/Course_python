#looping

# To execute logic multiple times
# python has 2 loop commands
# similar to if statements, a loops evaluate to true or false
# a loop is executing while the condition is true

#create a function for give 3 times thank you and after 1000 times thank you !!!

condition_thank = True
num = 0

def thank_you(condition_thank, num):
    while condition_thank == True:
        return print("Thank you very much !!!")
        num = num + 1
        if num ==  3:
            condition_thank = False #as is false finished the loop


