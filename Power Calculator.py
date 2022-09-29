from tkinter import Y


def main():
    x = float(input("What is X? "))
    y = float(input("What power do you want? "))

    print("The answer is ", round((cube(x, 3)), 8))
    
    
def cube(n, y):
    return pow(n, y)


main()