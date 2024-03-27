from tkinter import *
from PIL import Image,ImageTk

window = Tk()
window.title("Animal")

img_1 = ImageTk.PhotoImage(Image.open("Image view app/tiger.png"))
img_2 = ImageTk.PhotoImage(Image.open("Image view app/panda.jpeg"))
img_3 = ImageTk.PhotoImage(Image.open("Image view app/lion.jpeg"))

img_lst = [img_1,img_2,img_3]

#Adding status bar
status = Label(window, text="Image 1 of"+str(len(img_lst)),bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=img_1)
my_label.grid(row=0,column=0, columnspan=3)

def forward(image):
    global my_label
    global button_next
    global button_back
    global img_lst
 
    status = Label(window, text="Image "+ str(image)+ " of " + str(len(img_lst)),bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    my_label.grid_forget()
    my_label = Label(image=img_lst[image-1])
    button_next = Button(window,text=">>", command=lambda: forward(image+1))
    button_back = Button(window, text="<<",command=lambda: back(image-1))

    if image == len(img_lst):
        button_next = Button(window, text=">>", state=DISABLED)

    button_back.grid(column=0,row=1)
    button_next.grid(column=2,row=1)
    my_label.grid(row=0,column=0, columnspan=3)


def back(image):
    global my_label
    global button_next
    global button_back

    status = Label(window, text="Image "+ str(image)+ " of " + str(len(img_lst)),bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    my_label.grid_forget()
    my_label = Label(image=img_lst[image-1])
    button_next = Button(window,text=">>", command=lambda: forward(image+1))
    button_back = Button(window, text="<<",command=lambda: back(image-1))
    
    if image == 1:
        button_back = Button(window, text="<<", state=DISABLED)

    button_back.grid(column=0,row=1)
    button_next.grid(column=2,row=1)
    my_label.grid(row=0,column=0, columnspan=3)


button_back = Button(window, text="<<",command=back, state= DISABLED) 
button_exit = Button(window,text="EXIT", command=window.quit)
button_next = Button(window, text=">>",command=lambda: forward(2))

button_back.grid(column=0,row=1)
button_exit.grid(column=1,row=1)
button_next.grid(column=2,row=1, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
window.mainloop()