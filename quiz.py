print("Welcome to my computer quiz!")

playing = input("Are you ready to play the game? ")

if playing.title() != "Yes":
    print("Let start...!! ")

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

    print("You got " + str(score) + " answers!")
    print("Your score is " + str((score / 4) * 100) + "%.")
else:
    quit()    