import random
def play():
    num = random.randrange(1,21)
    trys = 10
    while (True):
            guessNumber = input("enter your guessed no.: ")
            try:
                if int(guessNumber)<num:
                    print("you guessed a smaller no. try again")
                    trys = trys-1
                    print("no. of chances left is",trys,"\n")
                elif int(guessNumber)>num:
                    print("you guessed a larger no. try again")
                    trys = trys-1
                    print("no. of chances left is",trys,"\n")
                elif int(guessNumber)==num:
                    print("you guessed it currect.\nyou took",trys,"chances\n")
                    conTinue()
                    break
            except:
                print("you entered a wrong input. try again")
                trys = trys-1
                print("no. of chances left is",trys,"\n")
            if trys == 0:
                print("you ran out of guesses\n")
                conTinue()
                break
def conTinue():
    print("do you want to play again")
    choice = input("enter y for yes or any other key to exit\n")
    if choice.lower()=="y":
        play()
    else:
        print("thank you")
play()
