from tkinter import *

window = Tk()

e = Entry(window, width= 60, border=5, borderwidth=4)
e.pack()
#.get() takes the input 
#.insert() already keeps a name
e.insert(0,"Type your name")



def clicked(): 
    label = Label (window, text="My name is "+e.get() ,font=("Times new roman",10))
    label.pack()
    
abutt = Button(window,text = "What is your name? ",
               padx= 10,
               pady=10,
               fg = "white",
               bg="black",
               activebackground="black", 
               activeforeground= "white",
               command= clicked
abutt.pack()

window.title("buttons and there works")

window.mainloop()
