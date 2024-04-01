from tkinter import *

#for images we have to import another library called pillow
from PIL import ImageTk,Image 

window = Tk()
window.title("Frames")
window.resizable(height=False, width= False)

frame = LabelFrame(window,text="this is my frame",padx=20, pady= 20)
frame.pack(padx=60, pady=60)

b = Button(frame,text="100")
b2 =Button(frame,text="200")
b.grid(row=0,column=0)
b2.grid(row=0, column=1)
window.mainloop()