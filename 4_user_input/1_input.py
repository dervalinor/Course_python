#input() - solicit data to the user

#create a function for ask name and show a message of welcome

def main():
    name = input("User name: ") 
    print("\n") #jump of line
    welcome(name)

def welcome(a):
    print(f"Welcome {a} to linux")

main()
