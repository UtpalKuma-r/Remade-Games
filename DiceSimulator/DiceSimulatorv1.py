import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()

window.title('Dice Simulator')
window.geometry('500x400')
window.config(bg='black')

DiceImageDict = {1:'images/1.png', 2:'images/2.png', 3:'images/3.png', 4:'images/4.png', 5:'images/5.png', 6:'images/6.png'}



def diceroll():
    image = DiceImageDict[random.randint(1, 6)]
    img = ImageTk.PhotoImage(Image.open(image))
    window.img = img
    canvas = tk.Canvas()


    canvas.create_image(100, 100, image=img)
    canvas.place(height=200, width = 200, x=156, y=50)

    tk.Button(text='Roll the Dice', command= lambda: diceroll()).place(x=210, y=300)



diceroll()

window.mainloop()