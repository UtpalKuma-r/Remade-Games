import random

def gameplay():
    try:      
        less = int(input("Enter smaller number: "))
        greater = int(input("Enter larger number: "))
    except:
        print("Only integers are allowed      1")                                             #1
        retry()
        
    try:
        winNumber = random.randint(less, greater)
    except:
        print("Cannot form a range as {less} is greater than {greater}     2")                       #2
        retry()

    p1guessNumber = 0
    p2guessNumber = 0

    guesswork = 0

    print(f"Player1:\nPlease guess the number from {less} to {greater}\n")


    try:
        while guesswork!=winNumber:
            guesswork = int(input("Enter your guessed number: "))
            p1guessNumber = p1guessNumber+1
            if guesswork == winNumber:
                print(f"you guessed it correct in {p1guessNumber} turns\n")
            elif guesswork < winNumber:
                print("You guessed a smaller number. Try Again\n")
            else:
                print("You guessed a larger number. Try Again\n")
        print("Thank you player1\n")


    except:
        print("Only integers are allowed                       3")                             #3
        retry()

    

    guesswork = 0

    print(f"Player2:\nPlease guess the number from {less} to {greater}")
    try:
        while guesswork!=winNumber:
            guesswork = int(input("Enter your guessed number: "))
            p2guessNumber = p2guessNumber+1
            if guesswork == winNumber:
                print(f"you guessed it correct in {p2guessNumber}\n")
            elif guesswork < winNumber:
                print("You guessed a smaller number. Try Again\n")
            else:
                print("You guessed a larger number. Try Again\n")

        print("Thank you player2\n")
        result(p1guessNumber, p2guessNumber)


    except Exception as e:
        print("Only Integers are excepted.              4\n", e)                                     #4
        retry()        
    
    

def winner(p1guessNumber, p2guessNumber):
        if p1guessNumber<p2guessNumber:
            return "player1"
        else:
            return "player2"


def result(p1guessNumber, p2guessNumber):
    print(f"number of guesses by Player1: {p1guessNumber}")
    print(f"number of guesses by Player2: {p2guessNumber}")
    print(f"{winner(p1guessNumber, p2guessNumber)} is the winner")
    retry()


def retry():
    print("Do you want to play again")
    choice = input("Enter y for yes or any other key to exit.")
    if choice.lower() == "y":
        gameplay()
    else:
        print("Thank You")
        exit()


gameplay()
    
