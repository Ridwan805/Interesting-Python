from tkinter import *
from PIL import ImageTk,Image 

food = ["pizza", "Hamburger", "hotdog"]

window = Tk()


x = IntVar()
x.set(100000)

for i in range(len(food)):
    radio = Radiobutton(window,
                        text = food[i],
                        variable=x,
                        value=i,
                        padx=25,
                        font=("yellow ginger",50),
                        indicatoron=0,  #eliminate circle indicator
                        width= 10
                        )
    radio.pack(anchor=W)
#from the broi code
window.mainloop()