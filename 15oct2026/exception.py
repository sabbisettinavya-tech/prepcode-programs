try:
    a=input("enter number 1:")
    b=input("enter number 2:")
    print(int(a)/int(b))
except ValueError:
    print("Give the Number as a input")
except ZeroDivisionError:
    print("cannot divide by zero")