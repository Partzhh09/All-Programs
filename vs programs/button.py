from tkinter import *

perent = Tk()

redbutton = Button(perent,text="red",fg="red")
redbutton.pack(side = LEFT)

redbutton = Button(perent,text="blue",fg="blue")
redbutton.pack(side = RIGHT)

redbutton = Button(perent,text="green",fg="green")
redbutton.pack(side = TOP)

redbutton = Button(perent,text="black",fg="black")
redbutton.pack(side = BOTTOM)

perent.mainloop()