def ask(): 
    a = int(input("First number: "))
    b = int(input("Second number: "))
    Result = sum_numbers(a, b)
    print(Result)

def sum_numbers(a, b): 
    return a + b
