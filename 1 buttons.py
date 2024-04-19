from tkinter import *

window = Tk()

def clicked():

    label = Label (window, text="Wow! I was clicked",font=("Times new roman",26))
    label.pack()

abutt = Button(window,text = "Unlock me🔓",
               padx= 10,
               pady=10,
               fg = "white",
               bg="black",
               activebackground="black", 
               activeforeground= "white",
               command= clicked)
abutt.pack()

window.title("buttons and there works")

window.mainloop()