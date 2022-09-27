def main():
    x = int(input("What is X? "))
    print("Cube of X is ", cube(x))
    
    
def cube(n):
    return pow(n, 3)


main()