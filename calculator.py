from tkinter import *

window = Tk()
window.title("Simple Calculator")

e = Entry(window, width= 35,borderwidth= 5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def Calculate(n):
    #e.delete(0, END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(n))

def clear():
    e.delete(0,END)
  
def adding():
    fn = e.get()
    global f_num 
    global math 
    math = "Addiiton"
    f_num = int(fn)
    e.delete(0,END)

def subtracting():
    fn = e.get()
    global f_num 
    global math 
    math = "Subtraction"
    f_num = int(fn)
    e.delete(0,END)

def multiply():
    fn = e.get()
    global f_num 
    global math 
    math = "Multiplication"
    f_num = int(fn)
    e.delete(0,END)

def divide():
    fn = e.get()
    global f_num 
    global math 
    math = "Division"
    f_num = int(fn)
    e.delete(0,END)

def Equal():
    sn = e.get()
    e.delete(0,END)
    if math == "Addiiton":
       e.insert(0, f_num + int(sn))
    if math == 'Subtraction':
       e.insert(0, f_num - int(sn))
    if math == "Multiplication":
       e.insert(0, f_num*int(sn))
    if math == 'Division':
       e.insert(0, f_num / int(sn))
    

#defining buttons
button_1= Button(window, 
                 text = "1",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(1),
                 borderwidth= 5)

button_2= Button(window, 
                 text = "2",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(2),
                 borderwidth= 5)

button_3= Button(window, 
                 text = "3",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(3),
                 borderwidth= 5)

button_4= Button(window, 
                 text = "4",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(4),
                 borderwidth= 5)

button_5= Button(window, 
                 text = "5",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(5),
                 borderwidth= 5)

button_6= Button(window, 
                 text = "6",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(6),
                 borderwidth= 5)

button_7= Button(window, 
                 text = "7",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(7),
                 borderwidth= 5)

button_8= Button(window, 
                 text = "8",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(8),
                 borderwidth= 5)

button_9= Button(window, 
                 text = "9",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(9),
                 borderwidth= 5)

button_0= Button(window, 
                 text = "0",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(0),
                 borderwidth= 5)

button_add= Button(window, 
                 text = "+",
                 padx = 39, 
                 pady= 20,
                 command = adding,
                 borderwidth= 5)
button_equal= Button(window, 
                 text = "=",
                 padx = 91, 
                 pady= 20,
                 command=  Equal,
                 borderwidth= 5)

button_subtrac= Button(window, 
                 text = "-",
                 padx = 39, 
                 pady= 20,
                 command=  subtracting,
                 borderwidth= 5)

button_divide= Button(window, 
                 text = "/",
                 padx = 39, 
                 pady= 20,
                 command=  divide,
                 borderwidth= 5)

button_multiply= Button(window, 
                 text = "x",
                 padx = 39, 
                 pady= 20,
                 command=  multiply,
                 borderwidth= 5)


button_clear= Button(window, 
                 text = "Clear",
                 padx = 79, 
                 pady= 20,
                 command=  clear,
                 borderwidth= 5)

#putting the buttons on the interface
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row= 4, column= 1,columnspan= 3)


button_add.grid(row = 5,column = 0)
button_equal.grid(row = 5,column = 1,columnspan= 3)

button_subtrac.grid(row= 6, column=  0)
button_multiply.grid(row= 6, column= 1)
button_divide.grid(row= 6, column=  2)

    

window.mainloop()