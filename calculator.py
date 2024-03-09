from tkinter import *

window = Tk()
window.title("Simple Calculator")

e = Entry(window, width= 35,borderwidth= 5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def Calculate(n):
    return

#defining buttons
button_1= Button(window, 
                 text = "1",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(),
                 borderwidth= 5)

button_2= Button(window, 
                 text = "2",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(),
                 borderwidth= 5)

button_3= Button(window, 
                 text = "3",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(),
                 borderwidth= 5)

button_4= Button(window, 
                 text = "4",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(),
                 borderwidth= 5)

button_5= Button(window, 
                 text = "5",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(),
                 borderwidth= 5)

button_6= Button(window, 
                 text = "6",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(),
                 borderwidth= 5)

button_7= Button(window, 
                 text = "7",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(),
                 borderwidth= 5)

button_8= Button(window, 
                 text = "8",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(),
                 borderwidth= 5)

button_9= Button(window, 
                 text = "9",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(),
                 borderwidth= 5)

button_0= Button(window, 
                 text = "0",
                 padx = 40, 
                 pady= 20,
                 command= lambda: Calculate(),
                 borderwidth= 5)

button_op1= Button(window, 
                 text = "+",
                 padx = 39, 
                 pady= 20,
                 command= lambda: Calculate(),
                 borderwidth= 5)
button_op2= Button(window, 
                 text = "=",
                 padx = 91, 
                 pady= 20,
                 command= lambda: Calculate(),
                 borderwidth= 5)

button_clear= Button(window, 
                 text = "Clear",
                 padx = 79, 
                 pady= 20,
                 command= lambda: Calculate(),
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


button_op1.grid(row = 5,column = 0)
button_op2.grid(row = 5,column = 1,columnspan= 3)


    


window.title("buttons and there works")

window.mainloop()