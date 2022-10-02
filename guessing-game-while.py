import random

i = random.randint(0, 9)
tries = 3
print(i)
while (True):
    x = int(input("Enter a number : "))
    if (x==i):
        print("This Is Your number ", x)
        break
    elif (x != i):
        tries -= 1 
        print("It is not you number, you have " + str(tries) +  " tries left")
        if (tries == 0):
            print("Bhaag idhr se")
            break
    
        
        