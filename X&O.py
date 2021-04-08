import tkinter as tk
import random as r


root = tk.Tk()

root.title("X & O")
root.geometry("300x300")


turnNumber = 0

def winCheck(player):
    if player.lower() == 'computer':
        checkList = computerChoicesList
    else:
        checkList = playerChoicesList
    
    for i in range(len(winComboList)):
        if winComboList[i][0] in checkList and winComboList[i][1]in checkList and winComboList[i][2] in checkList:
            return True
    else:
        return False


def computerChoice():
    player = 'computer'
    btn = r.choice(buttonList)
    mainControl(btn, player)


def mainControl(buttonName, player):
    global turnNumber
    
    if turnDecider(turnNumber, player):
        changeText(buttonName, player)
        if player.lower() == 'computer':
            computerChoicesList.append(buttonName)
        else:
            playerChoicesList.append(buttonName)
        buttonList.remove(buttonName)
        turnNumber += 1
    
    if winCheck(player):
        result(player)

    elif len(buttonList) == 0:
        result('no one')

    elif turnDecider(turnNumber, 'computer'):
        computerChoice()
      

def changeText(buttonName, player):
    if player.lower() == 'computer':
        buttonName.config(text = 'O')
    else:
        buttonName.config(text = 'X')
    

def turnDecider(turnNumber, player):

    if turnNumber%2 == 0:
        turn = 'User'
    else:
        turn = 'Computer'
    
    if turn.lower() == player.lower():
        return True
    else:
        return False


def result(player):
    displayResult.config(text = f'game over\n{player} wins')


b1 = tk.Button(root, text = "", command = lambda:mainControl(b1, 'user'))
b1.grid(row = 0, column = 0)
tk.Label(root, text = "|").grid(row = 0, column = 1)
b2 = tk.Button(root, text = "", command = lambda:mainControl(b2, 'user'))
b2.grid(row = 0, column = 2)
tk.Label(root, text = "|").grid(row = 0, column = 3)
b3 = tk.Button(root, text = "", command = lambda:mainControl(b3, 'user'))
b3.grid(row = 0, column = 4)

tk.Label(root, text = "-").grid(row = 1, column = 0)
tk.Label(root, text = "-").grid(row = 1, column = 1)
tk.Label(root, text = "-").grid(row = 1, column = 2)
tk.Label(root, text = "-").grid(row = 1, column = 3)
tk.Label(root, text = "-").grid(row = 1, column = 4)


b4 = tk.Button(root, text = "", command = lambda:mainControl(b4, 'user'))
b4.grid(row = 2, column = 0)
tk.Label(root, text = "|").grid(row = 2, column = 1)
b5 = tk.Button(root, text = "", command = lambda:mainControl(b5, 'user'))
b5.grid(row = 2, column = 2)
tk.Label(root, text = "|").grid(row = 2, column = 3)
b6 = tk.Button(root, text = "", command = lambda:mainControl(b6, 'user'))
b6.grid(row = 2, column = 4)

tk.Label(root, text = "-").grid(row = 3, column = 0)
tk.Label(root, text = "-").grid(row = 3, column = 1)
tk.Label(root, text = "-").grid(row = 3, column = 2)
tk.Label(root, text = "-").grid(row = 3, column = 3)
tk.Label(root, text = "-").grid(row = 3, column = 4)

b7 = tk.Button(root, text = "", command = lambda:mainControl(b7, 'user'))
b7.grid(row = 4, column = 0)
tk.Label(root, text = "|").grid(row = 4, column = 1)
b8 = tk.Button(root, text = "", command = lambda:mainControl(b8, 'user'))
b8.grid(row = 4, column = 2)
tk.Label(root, text = "|").grid(row = 4, column = 3)
b9 = tk.Button(root, text = "", command = lambda:mainControl(b9, 'user'))
b9.grid(row = 4, column = 4)

displayResult = tk.Label(root, text = '')
displayResult.grid(row = 6, column = 2)


buttonList = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
winComboList = [[b1,b2,b3],[b1,b4,b7],[b1,b5,b9],[b2,b5,b8],[b3,b6,b9],[b3,b5,b7],[b4,b5,b6],[b7,b8,b9]]
playerChoicesList = []
computerChoicesList = []


root.mainloop()
