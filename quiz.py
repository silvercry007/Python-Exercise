print("Welcome to my computer quiz!")

playing = input("Do you want to play? yes or no - ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is the capital of india?  ")
if answer.title() == "New Delhi":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How many states are in India ? ")
if answer.title() == "28":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How many Union Territories are in India ? ")
if answer.title() == "8":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the National animal of India ? ")
if answer.title() == "Tiger":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")