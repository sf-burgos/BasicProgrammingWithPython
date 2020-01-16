import turtle
import math
turtle.screensize(1000,1000)
turtle.pensize(10)

def seno(x,lista,amplitud,funcion,variable,reflexionx,corrimientox,reflexiony,corrimientoy):
    turtle.speed(1000)
    turtle.screensize(x,x)
    turtle.pensize(10)
    turtle.penup()
    turtle.goto(-x,0)
    turtle.pendown()
    for i in range(-x,x,50):
        turtle.pencolor('green')
        x=amplitud*(math.sin(i+corrimientox))+corrimientoy
        turtle.goto(i,100*x)
        break
        




