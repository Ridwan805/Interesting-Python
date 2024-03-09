from tkinter import *


window = Tk()
window.title("Sorting hat")
window.geometry("900x400")


    
def q1(n):
    
    global griff 
    global sly
    global raven
    global huff
    global question_1
    global button_1
    global button_2
    
    griff = 0
    sly = 0
    raven = 0
    huff = 0
    
    if n == "Dawn":
        griff = 2
        huff = 2 
    else:
        sly = 2
        raven = 2 
    question_1.destroy()
    button_1.destroy()
    button_2.destroy() 
    question_2 = Label(window, text = "Q2) When I'm dead, I want people to remember me as:",font=("Times new Roman",25) )
    question_2.pack()
    button_3 = Button(window, text= "1) The Good", padx= 40, pady=20,borderwidth=4,command=lambda: q2( "good"))
    button_4 = Button(window, text= "2) The Great", padx= 40, pady=20,borderwidth=4,command=lambda: q2( "great"))
    button_5 = Button(window, text= "3) The Wise", padx= 40, pady=20,borderwidth=4,command=lambda: q2( "wise"))
    button_6 = Button(window, text= "4) The Bold", padx= 40, pady=20,borderwidth=4,command=lambda: q2( "bold"))
    button_3.pack()
    button_4.pack()
    button_5.pack()
    button_6.pack()

    def q2(n):
        global griff 
        global sly
        global raven
        global huff

        if n == "good":
          huff += 3
        elif n == "great":
          sly += 3
        elif n == "wise":
          raven += 3
        elif n == "bold":
          griff += 3

        question_2.destroy()
        button_3.destroy()
        button_4.destroy()
        button_5.destroy()
        button_6.destroy()
        question_3 = Label(window, text = "Q3) Which kind of instrument most pleases your ear?",font=("Times new Roman",25) )
        question_3.pack()
        button_7 = Button(window, text= "1) The violin", padx= 45, pady=20,borderwidth=4,command=lambda: q3( "violin"))
        button_8 = Button(window, text= "2) The trumpet", padx= 38, pady=20,borderwidth=4,command=lambda: q3( "trumpet"))
        button_9 = Button(window, text= "3) The piano", padx= 44, pady=20,borderwidth=4,command=lambda: q3( "piano"))
        button_10 = Button(window, text= "4) The drum", padx= 45, pady=20,borderwidth=4,command=lambda: q3( "drum"))
        button_7.pack()
        button_8.pack()
        button_9.pack()
        button_10.pack()

        def q3(n):
            global griff 
            global sly
            global raven
            global huff
            global button_11

            if n == "trumpet":
                huff += 4
            elif n == "violin":
                sly += 4
            elif n == "piano":
                raven += 4
            elif n == "drum":
                griff += 4
            question_3.destroy()
            button_7.destroy()
            button_8.destroy()
            button_9.destroy()
            button_10.destroy()

            question_4 = Label(window, text="What would like for an activity?",font=("Times new Roman",25))
            question_4.pack()
            button_13 = Button(window, text= "1) Working with plants", padx= 45, pady=20,borderwidth=4,command=lambda: q4( "plants"))
            button_14 = Button(window, text= "2) Strategic thinking", padx= 45, pady=20,borderwidth=4,command=lambda: q4( "stra"))
            button_15 = Button(window, text= "3) Going on an Adventure", padx= 45, pady=20,borderwidth=4,command=lambda: q4( "adventure"))
            button_16 = Button(window, text= "4) Solving puzzles", padx= 45, pady=20,borderwidth=4,command=lambda: q4( "puzzles"))
            button_13.pack()
            button_14.pack()
            button_15.pack()
            button_16.pack()
            
            def q4(n):
                global griff 
                global sly
                global raven
                global huff
                global button_11
                global done
                if n == "plants":
                  huff += 3
                elif n == "stra":
                    sly += 3
                elif n == "puzzles":
                    raven += 3
                elif n == "adventure":
                    griff += 3

                question_4.destroy()
                button_13.destroy()
                button_14.destroy()
                button_15.destroy()
                button_16.destroy()
                
                question_5 = Label(window, text="Who was the founder of THE HOUSE HUFFLEPUFF?",font=("Times new Roman",25))
                question_5.pack()
                e = Entry(window, width= 60, border=5, borderwidth=4)
            
                e.pack()
                x = e.get()
                x.upper()    
                button_17 = Button(window, text= "Next", padx= 45, pady=20,borderwidth=4,command=lambda: q5(x))
                button_17.pack()
                def q5(n):
                  global griff 
                  global sly
                  global raven
                  global huff
                  global button_11
                  global done 
      
                  if n == 'HELGA HUFFLEPUFF':
                    huff += 10;
                  else:
                    huff -= 3
                  e.destroy()
                  question_5.destroy()
                  button_17.destroy()
                              
                  button_11 = Button(window, text= "Who won?",font=("Times new roman", 25), padx= 60, pady=30,borderwidth=4,command= veri)
                  button_11.place(x = 295, y = 140)
        
def veri():
  global griff 
  global sly
  global raven
  global huff
  global button_11
  global button_12
  global done

  dic = {"Griffindor" : griff,"Hufflepuff": huff, "Ravenclaw" : raven, "Slytherin" : sly} 

  maxy = 0
  win = ''
  for i in dic.items():
      if i[1] > maxy:
          maxy = i[1]
          win = i[0]
  
  done = Label(window,text="Congratulations! You're a " + win.upper(),font=("Times new Roman",25))
  done.place(x = 180, y = 150)
  button_11.destroy()
  button_12 = Button(window, text= "Reset", padx= 45, pady=20,borderwidth=4,command= reset)
  button_12.pack(side= "bottom")

def reset():
    global button_12
    global done
    global question_1
    global button_1
    global button_2

    done.destroy()
    button_12.destroy()
    question_1 = Label(window, text = "Q1) Do you like dawn or dusk?",font=("Times new Roman",25) )
    question_1.pack()

    button_1 = Button(window, text= "a) Dusk", padx= 40, pady=20,borderwidth=4,command=lambda: q1( "Dusk"))
    button_2 = Button(window, text= "b) Dawn", padx= 40, pady=20,borderwidth=4,command=lambda: q1( "Dawn"))
    button_1.pack()
    button_2.pack()
   

        


question_1 = Label(window, text = "Q1) Do you like dawn or dusk?",font=("Times new Roman",25) )
question_1.pack()

button_1 = Button(window, text= "a) Dusk", padx= 40, pady=20,borderwidth=4,command=lambda: q1( "Dusk"))
button_2 = Button(window, text= "b) Dawn", padx= 40, pady=20,borderwidth=4,command=lambda: q1( "Dawn"))
button_1.pack()
button_2.pack()



window.mainloop()