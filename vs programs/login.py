from tkinter import *

Window = Tk()

Window.title("wellcome to")
Window.geometry("350x200")

lbl = Label(Window,text="Username")
lbl.grid(column = 0,row = 0)
txt = Entry(Window,width = 10)
txt.grid(column = 1,row = 0)
lbl = Label(Window,text="Password")
lbl.grid(column = 0,row = 1)
txt = Entry(Window,width = 10)
txt.grid(column = 1,row = 1)

def clicked():
    print("Hello wellcome sir")
    
btn = Button(Window,text="click me",command=clicked)
btn.grid(column=1,row=3)
Window.mainloop()