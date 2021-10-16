#input() - solicit data to the user

#create a function for ask to the user two numbers

def main():
    print("Give me two numbers: ")
    a = input("a: ")
    b = input("b: ")
    suma(a, b)

def suma(a, b):
    print(f"Sum of {a} and {b}: {a + b}")

main()
