import turtle
import math
turtle.screensize(100000,1000000)
turtle.pensize(10)
def tan():
    turtle.penup()
    turtle.goto(-1000,0)
    turtle.pendown()
    for i in range(-1000,1000,50):
        turtle.pencolor('green')
        x=math.tan(i)
        turtle.goto(i,200*x)
