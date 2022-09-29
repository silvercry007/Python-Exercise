import random


i = random.randint(0, 9)

while (True):
    x = int(input("Enter a number : "))
    if (x==i):
        print("This Is Your number ", x)
        break
    else :
        print("It is not you number")
        
        