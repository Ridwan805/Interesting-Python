from tkinter import *
from PIL import ImageTk,Image


window = Tk()
window.title("New Window")
window.iconbitmap("images/cal.ico")

def open():
    global my_img

    top = Toplevel() # creates a new window
    top.title("new title")

    my_img = ImageTk.PhotoImage(Image.open("Image view app/lion.jpeg"))

    my_label = Label(top, image= my_img)
    my_label.pack()
    
    btn2 = Button(top,text= "close the second window", command= top.destroy)
    btn2.pack()

    top.mainloop()

btn = Button(window,text= "open second Window",command=open)
btn.pack()



window.mainloop()