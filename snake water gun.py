import random
choices = ["snake","water","gun"]
computerWin = 0
playerWin = 0
drawRound = 0
turn = 1
i = 10
while i>0:
    computerChoice = random.choice(choices)
    userChoice = input(f"round number {turn}\nenter your choice\ns for snake, w for water, g for gun: ")
    if userChoice.lower() == "s":
        if computerChoice == "snake":
            print(f"computer choice is {computerChoice} \n ROUND DRAW\n")
            turn = turn+1
            i = i-1
            drawRound = drawRound+1
        elif computerChoice == "water":
            print(f"computer choice is {computerChoice}\nYOU WON THIS ROUND\n")
            turn = turn+1
            i=i-1
            playerWin = playerWin+1
        else:
            print(f"computer choice is {computerChoice}\nYOU LOSS THIS ROUND\n")
            turn = turn+1
            i=i-1
            computerWin = computerWin+1
    elif userChoice.lower() == "w":
        if computerChoice == "water":
            print(f"computer choice is {computerChoice} \n ROUND DRAW\n")
            turn = turn+1
            i = i-1
            drawRound = drawRound+1
        elif computerChoice == "gun":
            print(f"computer choice is {computerChoice}\nYOU WON THIS ROUND\n")
            turn = turn+1
            i=i-1
            playerWin = playerWin+1
        else:
            print(f"computer choice is {computerChoice}\nYOU LOSS THIS ROUND\n")
            turn = turn+1
            i=i-1
            computerWin = computerWin+1
    elif userChoice.lower() == "g":
        if computerChoice == "gun":
            print(f"computer choice is {computerChoice} \n ROUND DRAW\n")
            turn = turn+1
            i = i-1
            drawRound = drawRound+1
        elif computerChoice == "snake":
            print(f"computer choice is {computerChoice}\nYOU WON THIS ROUND\n")
            turn = turn+1
            i=i-1
            playerWin = playerWin +1
        else:
            print(f"computer choice is {computerChoice}\nYOU LOSS THIS ROUND\n")
            turn = turn+1
            i=i-1
            computerWin = computerWin+1
    else:
        print(f"computer choice is {computerChoice}\nYOU LOSS THIS ROUND as you enter a wrong input\n")
        turn = turn+1
        i=i-1
        computerWin = computerWin+1
print(f"Game Over\ncomputer win = {computerWin}\nplayer win = {playerWin}\ndraw round(s) = {drawRound}")
