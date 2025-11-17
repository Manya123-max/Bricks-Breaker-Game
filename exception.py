def handlingZero():
    try:
        a = int(input("enter the first number="))
        b = int(input("enter the second number="))
        div = a / b
        print(div)

    except ZeroDivisionError:
        print("You cannot divide any no with zero")


def handlingType():
    try:
        c = int(input("enter the first number="))
        d = int(input("enter the second number="))
        add = 'c' + d
        print(add)

    except TypeError:
        print("Attempted opeartion is not supported can only concate str to str")


def handlingValue():
    try:
        x = int(input("Please Enter a number :"))

    except ValueError:
        print("Oops! that was not vaild number. Try again....")


def handlingArgument():
    try:
        def square(x):
            x = int(input('enter no'))
            print(x ** 2)
            print(square(x, y))
    except:
        print("Oops! that was an extra argument. Try again....")


def handlingIndex():
    list = input("Enter a list of number 5 seperate by commas:").split(",")
    try:
        print(list[100])
    except IndexError:
        print("index out of range...")


def error_func():
    print("Options:")
    print("enter 'z' for ZeroDivisionError")
    print("enter 't' for TypeError")
    print("enter 'v' for ValueError")
    print("enter 'a' for ArgumentError")
    print("enter 'i' for IndexError")

    while True:
        user_input = input(":")

        if user_input == "quit":
            break
        elif user_input in ['z', 't', 'v', 'a', 'i']:

            if user_input == 'z':
                print("Result:", handlingZero())
            elif user_input == "t":
                print("Result:", handlingType())
            elif user_input == "v":
                print("Result:", handlingValue())
            elif user_input == "a":
                print("Result:", handlingArgument())
            elif user_input == "i":
                print("Result:", handlingIndex())
        else:
            print("Invalid input. Please try again.")


error_func()

