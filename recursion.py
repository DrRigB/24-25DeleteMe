#Bellow is an example of recursion


def my_recursion():
    choice = input("would you like to play a game, y or n: ")
    if(choice == "y"):
        my_recursion()
    elif(choice == "n"):
        print("Have a lovley day.")
    else:
        print("I couldn't quite get that. Please only use y or n")
        my_recursion()

my_recursion()
