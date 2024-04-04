from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

window = Tk()

#types of message box showinfo, showwarning, showerror, askquestion, askokcancel,askyesorno

def popup():
    messagebox.showinfo("This is my popup!","Hello")

Button(window, text="popup", command=popup).pack()

window.title("Message")
window.mainloop()