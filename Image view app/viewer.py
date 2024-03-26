from tkinter import *
from PIL import Image,ImageTk

window = Tk()
window.title("Animal")

img_1 = ImageTk.PhotoImage(Image.open("Image view app/tiger.png"))
img_2 = ImageTk.PhotoImage(Image.open("Image view app/panda.jpeg"))
img_3 = ImageTk.PhotoImage(Image.open("Image view app/lion.jpeg"))

img_lst = [img_1,img_2,img_3]

my_label = Label(image=img_1)
my_label.grid(row=0,column=0, columnspan=3)

window.mainloop()