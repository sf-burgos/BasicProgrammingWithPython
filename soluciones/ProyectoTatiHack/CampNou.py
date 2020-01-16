from sys import stdin
import turtle
import random
#from turtle import *
from CampNou import *

def camp():
    turtle.title("TactiHack")
    turtle.bgcolor("#000000")
    turtle.up()
    turtle.screensize(5000,3000)#screensize 
    turtle.hideturtle()#make the turtle invisible 
    #cuadro 
    turtle.speed(1000)
    turtle.color("#00A510")
    turtle.pencolor("#FFFFFF")
    turtle.pensize(15)
    turtle.goto(-600,310)
    turtle.pd()
    turtle.begin_fill()
    turtle.forward(1200)
    turtle.right(90)
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(1200)
    turtle.right(90)
    turtle.forward(600)
    turtle.end_fill()
    
    #circulo
    turtle.pu()
    turtle.pencolor("#FFFFFF")
    turtle.pensize(5)
    turtle.goto(60,10)
    turtle.pd()
    turtle.circle(60)
    #linea media
    turtle.pu()
    turtle.goto(0,310)
    turtle.pd()
    turtle.goto(0,-290)
    #areas
    turtle.pu()
    turtle.goto(-600,160)
    turtle.pd()
    turtle.rt(90)
    camp2(200,300)
    
    turtle.pu()
    turtle.goto(-600,90)
    turtle.rt(90)
    camp2(130,165)

    turtle.pu()
    turtle.goto(-400,-40)
    turtle.rt(90)
    turtle.pd()
    #turtle.circle(120, 90) esquina
    turtle.circle(60, 180)

    turtle.pu()
    turtle.goto(600,-140)
    
    turtle.pd()
    turtle.rt(360)
    camp2(200,300)

    turtle.pu()
    turtle.goto(600,-70)
    turtle.rt(90)
    camp2(130,165)
    
    turtle.pu()
    turtle.goto(400,75)
    turtle.rt(90)
    turtle.pd()
    turtle.circle(60, 180)

    turtle.pu()
    turtle.goto(600,-245)
    turtle.rt(180)
    turtle.pd()
    turtle.circle(50, 90)
    
    turtle.pu()
    turtle.goto(-600,245)
    turtle.rt(270)
    turtle.pd()
    turtle.circle(50, 90)

    turtle.pu()
    turtle.goto(555,310)
    turtle.rt(180)
    turtle.pd()
    turtle.circle(50, 90)

    turtle.pu()
    turtle.goto(-555,-290)
    turtle.rt(270)
    turtle.pd()
    turtle.circle(50, 90)
    #estrella()
    turtle.pu()
    turtle.goto(0,10)
    turtle.rt(180)
    
def estrella():
    turtle.goto(600,300)
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    turtle.speed(1000)
    while True:
        turtle.forward(100)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()


    
def camp2(x,y):
    turtle.pencolor("#FFFFFF")
    turtle.pd()
    turtle.forward(x)#largo1
    turtle.right(90)
    turtle.forward(y)#ancho1
    turtle.right(90)
    turtle.forward(x)#largo2
    turtle.right(90)
    turtle.forward(y)#ancho2

