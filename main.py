from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    window.config(bg=colorHex)
    text = Text(window, font=("Times New Roman", 20, "bold"), fg="White", bg="Red")
    text.pack()
    

window = Tk()

button = Button(window, text="Click to choose color", command=click)
button.pack()

window.mainloop()