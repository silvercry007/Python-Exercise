import random

i = random.randint(0, 9)
tries = 3
points = 100
print(i)
while (True):
    x = int(input("Enter a number : "))
    if (x==i):
        print("This Is Your number ", x , " You have ", points, " Points")
        break
    elif (x != i):
        tries -= 1
        if (points == 100):
            points = points - 20
        elif (points == 80):
            points = points - 30
        print("It is not you number, you have " + str(tries) +  " tries left")
        if (tries == 0):
            print("Too bad, you earned 0 points. Better Luck next time")
            break