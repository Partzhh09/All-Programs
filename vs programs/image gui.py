from tkinter import *

top = Tk()

c = Canvas(top,bg="blue",height=250,width=300)
filename = PhotoImage(file = "D:\\parth\\GUI\\Earth.gif")
background_label = Label(top,image=filename)

background_label.place(x=0,y=0,relwidth=1,relheight=1)

c.pack()
top.mainloop()