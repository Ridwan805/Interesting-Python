from tkinter import *
from PIL import ImageTk,Image


window = Tk()
window.iconbitmap("Sorting hat\imageshat.ico")
window.title("Sorting hat")
window.geometry("900x514")

image2 = ImageTk.PhotoImage(Image.open("Sorting hat\images\2.png"))
image3 = ImageTk.PhotoImage(Image.open("Sorting hat\images\3.png"))
image4 = ImageTk.PhotoImage(Image.open("Sorting hat\images\4.png"))
image5 = ImageTk.PhotoImage(Image.open("Sorting hat\images\5.png"))
image6 = ImageTk.PhotoImage(Image.open("Sorting hat\images\6.png"))
image7 = ImageTk.PhotoImage(Image.open("Sorting hat\images\7.png"))
image8 = ImageTk.PhotoImage(Image.open("Sorting hat\images\8.png"))
image9 = ImageTk.PhotoImage(Image.open("Sorting hat\images\9.png"))
image10 =ImageTk.PhotoImage(Image.open("Sorting hat\images\10.png"))
imagewin = ImageTk.PhotoImage(Image.open("Sorting hat\images\2.png"))

imagegriff = ImageTk.PhotoImage(Image.open("Sorting hat\images\griff.png"))
imagesly = ImageTk.PhotoImage(Image.open("Sorting hat\images\sly.png"))
imageraven = ImageTk.PhotoImage(Image.open("Sorting hat\images\raven.png"))
imagehuff = ImageTk.PhotoImage(Image.open("Sorting hat\images\huff.png"))

def intro_next():

  global house
  global letsgo

  global intro
  global intro_button
  global one
  global two

  one.destroy()
  intro.destroy()
  intro_button.destroy()

  
  two = Label(image = image2)
  

  house = Label(window, text = "Let's put you in a house\nWith the Sorting Hat",font=("Times new Roman",18))
  house.pack()
  letsgo = Button(window, text= "LESSGOOOO", padx= 40, pady=12,command= putting_house)
  letsgo.place(x= 380,y=462)
  two.pack()

def putting_house():
    global house
    global letsgo

    global question_1
    global button_1
    global button_2

    global intro
    global intro_button
    global two
    global three
    
    house.destroy()
    letsgo.destroy()
    two.destroy()

    three = Label(window, image= image3)
    
    question_1 = Label(window, text = "Q1) Do you like dawn or dusk?",font=("Times new Roman",25) )
    question_1.pack()

    button_1 = Button(window, text= "a) Dusk", padx= 41, pady=10,command=lambda: q1( "Dusk"))
    button_2 = Button(window, text= "b) Dawn", padx= 40, pady=10,command=lambda: q1( "Dawn"))
    
    
    button_1.place(x=150,y=240)
    button_2.place(x=640,y=240)
    three.pack()
    
def q1(n):
    
    global griff 
    global sly
    global raven
    global huff

    global question_1
    global button_1
    global button_2

    global three
    global four

  

    global question_2
    global button_3
    global button_4
    global button_5
    global button_6
    
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
    three.destroy()
    
    four = Label(window,image= image4)

    question_2 = Label(window, text = "Q2) When I'm dead, I want people to remember me as:",font=("Times new Roman",25) )
    question_2.pack()
    button_3 = Button(window, text= "1) The Good", padx= 42, pady=20,command=lambda: q2( "good"))
    button_4 = Button(window, text= "2) The Great", padx= 40, pady=20,command=lambda: q2( "great"))
    button_5 = Button(window, text= "3) The Wise", padx= 43, pady=20,command=lambda: q2( "wise"))
    button_6 = Button(window, text= "4) The Bold", padx= 44, pady=20,command=lambda: q2( "bold"))
    button_3.place(x= 180,y= 70 )
    button_4.place(x = 600 ,y= 70)
    button_5.place(x = 180,y=340)
    button_6.place(x = 600,y=340)

    four.pack()

def q2(n):
    global griff 
    global sly
    global raven
    global huff

    global four
    global five

    global question_2
    global button_3
    global button_4
    global button_5
    global button_6

    global question_3
    global button_7
    global button_8
    global button_9
    global button_10



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
    four.destroy()

    five = Label(image = image5)
    
    question_3 = Label(window, text = "Q3) Which kind of instrument most pleases your ear?",font=("Times new Roman",25) )
    question_3.pack()
    button_7 = Button(window, text= "1) The violin", padx= 45, pady=20,command=lambda: q3( "violin"))
    button_8 = Button(window, text= "2) The trumpet", padx= 38, pady=20,command=lambda: q3( "trumpet"))
    button_9 = Button(window, text= "3) The piano", padx= 44, pady=20,command=lambda: q3( "piano"))
    button_10 = Button(window, text= "4) The drum", padx= 45, pady=20,command=lambda: q3( "drum"))
    button_7.place(x = 80, y = 120 )
    button_8.place(x = 650, y = 120)
    button_9.place(x = 80, y = 320)
    button_10.place(x = 650, y = 320) 

    five.place(relheight=1,relwidth=1)

def q3(n):
    global griff 
    global sly
    global raven
    global huff
    global button_11

    global question_4
    global button_13
    global button_14
    global button_15
    global button_16

    global question_3
    global button_7
    global button_8
    global button_9
    global button_10

    global five
    global six

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
    five.destroy()

    six = Label(image = image6)
    question_4 = Label(window, text="Q4) What would like for an activity?",font=("Times new Roman",25))
    question_4.pack()
    button_13 = Button(window, text= "1) Working with plants", padx= 45, pady=20,command=lambda: q4( "plants"))
    button_14 = Button(window, text= "2) Strategic thinking", padx= 45, pady=20,command=lambda: q4( "stra"))
    button_15 = Button(window, text= "3) Going on an Adventure", padx= 45, pady=20,command=lambda: q4( "adventure"))
    button_16 = Button(window, text= "4) Solving puzzles", padx= 45, pady=20,command=lambda: q4( "puzzles"))
    button_13.place(x = 80 , y =120)
    button_14.place(x = 620 , y =120)
    button_15.place(x = 80 , y =320)
    button_16.place(x = 620 , y =320)
    six.place(relwidth=1, relheight=1)
        
def q4(n):
    global griff 
    global sly
    global raven
    global huff

    global question_4
    global button_13
    global button_14
    global button_15
    global button_16
    
    global question_5
    global button_17
    global e

    global six
    global seven
    

    

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
    six.destroy()
    
    seven = Label(image=image7)
    question_5 = Label(window, text="Q5) Who was the founder of THE HOUSE HUFFLEPUFF?",font=("Times new Roman",25))
    question_5.pack()
    e = Entry(window, width= 60, border=5, borderwidth=4)
    e.pack(pady= 20, padx = 10)
    x = e.get()
    x.upper() 
    seven.place(relheight=1,relwidth=1)

    button_17 = Button(window, text= "Next", padx= 45, pady=20,command=lambda: q5(x))
    button_17.place(x = 400, y= 300)

def q5(n):
  global griff 
  global sly
  global raven
  global huff
  

  global question_5
  global button_17
  global e

  global question_6
  global button_18
  global button_19
  global button_20
  global button_21

  global seven
  global eight
  
  

  if n == 'HELGA HUFFLEPUFF':
    huff += 4;
  else:
    huff -= 3
  e.destroy()
  question_5.destroy()
  button_17.destroy()
  seven.destroy()

  eight = Label(image= image8)
  question_6 = Label(window, text="Q6) Who is the ghost of Gryffindor?",font = ("Times new Roman", 25))
  question_6.pack(side="top")

  button_18 = Button(window, text= "a) Fat Friar", padx= 54, pady=20,command= lambda: q6("fat"))
  button_19 = Button(window, text= "d) Bloody Baron", padx= 39, pady=20,command= lambda: q6('blood'))
  button_20 = Button(window, text= "c) Nearly Headless Nick", padx= 20, pady=20,command= lambda: q6('headless'))
  button_21 = Button(window, text= "b) The Grey Lady", padx= 40, pady=20,command= lambda: q6('grey'))
  eight.place(relheight=1,relwidth=1)

  button_18.place(x = 80, y=120)
  button_19.place(x = 620, y=320)
  button_20.place(x = 80, y=320)
  button_21.place(x = 620, y=120)

def q6(n):
  global griff 
  global sly
  global raven
  global huff
  global button_11

  global question_6
  global button_18
  global button_19
  global button_20
  global button_21

  global question_7
  global button_22
  global button_23
  global button_24
  global button_25

  global eight
  global nine

  if n == 'headless':
    griff += 4;
  else:
    griff -= 3

  question_6.destroy()
  button_18.destroy()
  button_19.destroy()
  button_20.destroy()
  button_21.destroy()
  eight.destroy()
  

  nine = Label(image= image9)
  question_7 = Label(window, text= "Q7) What rare gift Salazar Slytherine had?",font = ("Times new Roman", 25))
  question_7.pack()

  button_22 = Button(window, text= "a) Good at Quiditch",font=("Times new roman", 10), padx= 40, pady=20,command= lambda:q7("q"))
  button_23 = Button(window, text= "b) Good at Maths",font=("Times new roman", 10), padx= 40, pady=20,command= lambda:q7("m"))
  button_24 = Button(window, text= "c) Speak Parseltongue",font=("Times new roman", 10), padx= 40, pady=20,command= lambda:q7("p"))
  button_25 = Button(window, text= "b) Was Good Sword Man",font=("Times new roman", 10), padx= 40, pady=20,command= lambda:q7("s"))
  

  button_22.place(x = 80 , y =120)
  button_23.place(x = 620 , y =120)
  button_24.place(x = 80 , y =320)
  button_25.place(x = 620 , y =320)
  nine.place(relheight=1,relwidth=1)

def q7(n):
  global griff 
  global sly
  global raven
  global huff
  global button_11

  global question_7
  global button_22
  global button_23
  global button_24
  global button_25

  global question_8
  global button_26
  global button_27
  global button_28
  global button_29

  global nine
  global ten
  
  question_7.destroy()
  button_22.destroy()
  button_23.destroy()
  button_24.destroy()
  button_25.destroy()
  nine.destroy()

  if n == "p":
     sly += 4
  else:
     sly -=2
  
  ten = Label(image = image10)
  question_8 = Label(window, text ="Q8) Which one of the following a professor of Ravenclaw?", font = ("Times new roman",25))
  question_8.pack()
  
  button_26 = Button(window, text= "a) Professor Sprout", padx= 40, pady=20,command= lambda :q8("s")) 
  button_27 = Button(window, text= "b) Professor Filius Fitwick", padx= 40, pady=20,command= lambda: q8("f")) 
  button_28 = Button(window, text= "c) Professor McGonagall", padx= 40, pady=20,command= lambda: q8("m")) 
  button_29 = Button(window, text= "d) Professor Quirrell", padx= 40, pady=20,command= lambda : q8("q")) 
  
  button_26.place(x = 80 , y =120)
  button_27.place(x = 620 , y =120)
  button_28.place(x = 80 , y =320)
  button_29.place(x = 620 , y =320)
  ten.place(relheight=1,relwidth=1)

def q8(n):
  global griff 
  global sly
  global raven
  global huff
  global button_11

  global question_8
  global button_26
  global button_27
  global button_28
  global button_29

  global ten
  global eleven

  if n == "f":
     raven += 4
  else:
     raven -= 3

  ten.destroy()
  question_8.destroy()
  button_26.destroy()
  button_27.destroy()
  button_28.destroy()
  button_29.destroy()
  
  eleven = Label(image= imagewin)
  button_11 = Button(window, text= "Who won?", padx= 10, pady=15,command= veri)
  button_11.pack(side="bottom") 
  eleven.place(relheight=1,relwidth=1)

def veri():
  global griff 
  global sly
  global raven
  global huff
  global button_11
  global button_12
  global done
  global button_quit

  global eleven
  global winh
  
  eleven.destroy()
  
  dic = {"Griffindor" : griff,"Hufflepuff": huff, "Ravenclaw" : raven, "Slytherin" : sly} 

  maxy = 0
  win = ''
  for i in dic.items():
      if i[1] > maxy:
          maxy = i[1]
          win = i[0]
  
  if win.upper() == "HUFFLEPUFF":
     winh = Label(image= imagehuff)
  elif win.upper() == "GRIFFINDOR":
     winh = Label(image= imagegriff)

  elif win.upper() == "SLYTHERIN":
     winh = Label(image= imagesly)

  elif win.upper() == "RAVENCLAW":
     winh = Label(image= imageraven)


    
  
  done = Label(window,text="Congratulations! You're a " + win.upper(),font=("Times new Roman",25))
  done.pack(side = "top")
  button_11.destroy()
  button_12 = Button(window, text= "Reset", padx= 43, pady=10,command= reset,bg="green")
  button_12.place(x = 150,y = 465)
  button_quit = Button(window, text = "Quit",padx= 45, pady=10, command = window.quit,background="#8B0000")
  button_quit.place(x = 650, y = 465)
  winh.place(relheight=1,relwidth=1)

def reset():
    global button_12
    global done
    global intro
    global intro_button
    global button_quit

    global one
    global winh

    winh.destroy()
    one = Label(image = image1)
    button_quit.destroy()
    done.destroy()
    button_12.destroy()

    intro = Label(window, text = "Welcome to Howgwarts",font=("Times new Roman",25))
    intro.pack()
    intro_button = Button(window, text= "Next", padx= 40, pady=20,command=intro_next) 
    intro_button.place(x= 400,y=445)
    one.pack()



image1 = ImageTk.PhotoImage(Image.open("Sorting hat\images\1.png"))
one = Label(image = image1)


intro = Label(window, text = "Welcome to Howgwarts",font=("Times new Roman",25))
intro.pack()
intro_button = Button(window, text= "Next", padx= 40, pady=20,command=intro_next,background="green") 
intro_button.place(x= 400,y=445)
one.pack()

window.mainloop()