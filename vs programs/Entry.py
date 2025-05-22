from tkinter import *

Window = Tk()

Window.title("wellcome to")
Window.geometry("350x200")

lbl = Label(Window,text="Hello")
lbl.grid(column = 0,row = 0)
txt = Entry(Window,width = 10)
txt.grid(column = 1,row = 0)
def clicked():
    res = "Hello wellcome to " + txt.get()
    lbl.configure(text=res)
    
btn = Button(Window,text="click me",command=clicked)
btn.grid(column=2,row=0)
Window.mainloop()