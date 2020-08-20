#!/usr/bin/env python
'''

THIS IS A MINI-PROJECT BY THE LANDSCAPYX SOFTWARE TEAM AUTHOR: IDRISS CHADILI, PART
OF THE LANDSCAPYX SOFTWARE TEAM PLEASE SUPPORT US <3 BY LIKING OUR FACEBOOK
PAGE : LANDSCAPYX
OUR WEBSITE: https://landscapyxsoftwareteam.com ( Currently https://landscapyxsoftwareteam.wordpress.com )

                                          IMPORTANT:
___________________________________________________________________________________________________________________________                                          
THIS IS JUST A BASIC EXAMPLE, SO YOU WILL PLAY YOURSELF AGAINST YOURSELF, YOU CAN TRAIN YOURSELF FOR WINNING AGAINST
OTHERS BY SIMULATING MOVES. ANYWAY , YOU CAN IMPLEMENT A TIC TAC TOE ENGINE YOURSELF, HOWEVER, IF IT IS OK WITH YOU,
YOU CAN SHARE IT WITH OUR TEAM TROUGH OUR FACEBOOK PAGE: LANDSCAPYX.

PLEASE SHOW US SOME INTEREST :
    --> IF YOU DEVELOPED SOMETHING NEW USING THIS PROJECT, DON'T HESITATE TO SHARE IT WITH US
    --> VISIT OUR GITHUB TO SEE THE MOST POPULAR REPOSITORIES
    --> SUPPORT US IN OUR FACEBOOK PAGE: LANDSCAPYX

THIS GAME USES PYTHON TROUGH THE TURTLE MODULE DON'T HESITATE TE REPORT US OTHER BUGS AND SUGGESTIONS ON OUR FACEBOOK PAGE,
LANDSCAPYX. OR TO THE PUBLISHER OF THIS PROJECT, IDRISS CHADILI (Sasukethelast0) MAY YOU SUPPORT US :)
___________________________________________________________________________________________________________________________

'''
import turtle,random;turtle.colormode(255)
from tkinter import *  
from tkinter import messagebox  
s=turtle.Screen()
s.setup(600,500)
s.tracer(99,0)
s.bgcolor(64,64,64)
s.register_shape('selector.gif')
t=turtle.Turtle()
t.ht();t.speed(0)
t.penup()
t.goto(-120,125)
t.pendown()
t.pensize(3)
t.color((200,200,200),(64,64,64))

'''
Here, we just initialize the gaming board and the player. These functions will help us make the board. By the way, these function
can help you making other projects ;)
Please support us in our facebook page: LANDSCAPYX
'''

def square(a):
    t.begin_fill()
    for i in range(4):
        t.fd(a)
        t.rt(90)
    t.end_fill()

def gird(w,h,a):
    for y in range(h):
        for x in range(w):
            square(a)
            t.penup()
            t.fd(a)
            t.pendown()
        t.penup()
        t.goto(-120,t.ycor()-a)
        t.pendown()
        
gird(3,3,77)
t.penup()
t.goto(0,200)
t.write("BASIC TIC TAC TOE GAME", False, align="center",font=("Georgia", 25, "bold"))
t.goto(0,154)
t.color('cyan')
t.write("THIS IS A MINI PROJECT OF THE \nLANDSCAPYX SOFTWARE TEAM", False, align="center",font=("Georgia", 14, "normal"))
t.goto(0,135)
t.color('darkorange')
t.write("USE THE ARROWS TO PLAY THE GAME AND PRESS SPACE TO VALIDATE YOUR ACTION", False, align="center",font=("Georgia", 10, "normal"))

t.goto(0,-186)
t.color('orange')
t.write("      Please support us in our\n facebook page : LANDSCAPYX", False, align="center",font=("Georgia", 23, "bold"))
t.goto(0,-231)
t.color('magenta')
t.write("This game is about training by playing against\n                yourself and simulate moves ", False, align="center",
        font=("Georgia", 14, "normal"))

t=t.clone()
t.goto(-120+77/2+1,125-77/2-1)
t.shape('selector.gif')
t.showturtle()
s.tracer(1,7)

'''
Now, the 'game' will start, we will now set all the variables and all the stuff related to the game
Well, basically, this is the board:


******************Glossary************************
0 = None (Empty box that contains neither X nor O)
1 = X ( Box contains X )
2 = 0 ( Box contains O )

The MAP list contains only 0, because all the boxes are obviously empty, aren't they ? ;)
Please support us in our facebook page: LANDSCAPYX
*************************************************
'''

glossary={1:'X',2:'O'}
MAP = [
    
    [0,0,0],
    [0,0,0],                  
    [0,0,0]

    ]

X=Y=0
S=1
'''This is the position of the cursor, because the cursor can move only in the gaming board ;) The cursor is the blue square
that moves in the board ( Play the game so you can see it :D :) ;) )
Now, all these functions below will just move the cursor in the gaming board.
The 'S' variable can either be an X(1) or an O(2), here it is 1, so an X ;)
'''
def up():
    global X,Y,MAP,t
    if Y>0:
        t.sety(t.ycor()+77)
        Y-=1
def down():
    global X,Y,MAP,t
    if Y<2:
        t.sety(t.ycor()-77)
        Y+=1
def left():
    global X,Y,MAP,t
    if X>0:
        t.setx(t.xcor()-77)
        X-=1
def right():
    global X,Y,MAP,t
    if X<2 :
        t.setx(t.xcor()+77)
        X+=1
'''
Now, let us add a function that enables the player to make an 'X' or an 'O'. Mmmm... How we will do it??? Okay! Let's
do it when the player clicks on the space button OK?? Here we go ! When the player click on Space, we will call this
action 'validate' XD
The computer selection will be from the function called: 'computer' OK ? Here we go ;) 
'''
def validate():
    global X,Y,MAP,t,S
    if MAP[Y][X]==0:
        MAP[Y][X]=S
        xx,yy=t.xcor(),t.ycor()
        t.goto(xx,yy-77/2-1)
        t.write(glossary[S], False, align="center",font=("Arial", 51, "bold"))
        t.goto(xx,yy)
        if S==1:
            S=2
        else:
            S=1
        print(MAP)

    FINISHED=True
    for y in MAP:
        for x in y:
            if x==0:FINISHED=False
    if FINISHED:
        turtle.bye()
        top = Tk()
        top.geometry("1x1")
        top.withdraw()
        messagebox.showinfo("Game over!","Someone won the game!\nPlease support us on our facebook page :)\nRestart the script to run again.")  
        exit
      
s.onkey(up, "Up")
s.onkey(left, "Left")
s.onkey(right, "Right")
s.onkey(down, "Down")
s.onkey(validate, "space")
s.listen()
turtle.mainloop()
