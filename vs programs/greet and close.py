from tkinter import Tk, Label, Button
import sys

class myfirstGUI:
    def __init__(self,master):
        self.master = master
        master.title("GUI program")
        
        self.label = Label(master,text="Hello")
        self.label.pack()
        
        self.greet_button = Button(master,text="Greet",command = self.greet)
        self.greet_button.pack()
        
        self.close_button = Button(master,text="Close",command = master.quit)
        self.close_button.pack()
        
    def greet(self):
        print("Hello nice to meet you sir")
        
    def quit(self):
        sys.quit()
    
root = Tk()
mu_gui = myfirstGUI(root)
root.mainloop()