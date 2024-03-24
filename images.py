from tkinter import *

#for images we have to import another library called pillow
from PIL import ImageTk,Image 

window = Tk()

image1 = ImageTk.PhotoImage(Image.open("Tkinter/for/tiger.png"))
one =  Label(image = image1)
one.pack()
image2 = ImageTk.PhotoImage(Image.open("Tkinter/for/lion.jpeg"))
two =  Label(image = image2)
two.pack()
image3 = ImageTk.PhotoImage(Image.open("Tkinter/for/panda.jpeg"))
three =  Label(image = image3)
three.pack()

window.mainloop()