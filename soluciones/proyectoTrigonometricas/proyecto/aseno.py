#import turtle
import turtle
from math import *
#turtle.pensize(5)
"""PRE:los parametrors que necesita son: x es un entero el cual se lo dara la funcion main cuando sea necesario, para cambiar el tamaño de la pantalla(screensize) o el
valor del for para llevar a evaluar(eval) la funcion parte1 y parte2:lo retornara la entrada la cual la retornara la funcion (entrada()) la cual equivale del inicio a
x y de x al final de la ecuacion de la forma y=af(bx+-c)+-d
Pos: llevara la tortuga a graficar la funcion correspondiente a la entrada"""
def funcion(x,y,parte1,parte2):
    turtle.speed(1000)
    turtle.screensize(10000,10000)
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(10000,0)
    turtle.pendown()

    '''    if 'pi' in parte1:
        parte1=parte1.replace('pi','pi*10')

   '''
  
    valores=[]     
    for i in range(-1000,1001,25):
             
             turtle.pencolor('blue')
             y=eval(str(parte1)+str(i)+str(parte2))
             valores.append(y)
    
    maximo=max(valores)
    minimo=min(valores)
    color='blue'
    for i in range(-10000,10001,25):
             turtle.pencolor(color)
             y=eval(str(parte1)+str(i)+str(parte2))
             if i==0:
                 color='red'
                 print('amplitud: ',round(maximo,0))
             if y==0:
                 turtle.pencolor('black')
                 turtle.write(i/200, move=False, align="left", font=("Arial", 15, "normal"))
             if y==0:
                 print(turtle.pos())
             turtle.pencolor(color)
             turtle.goto((i/2)*-1,100*y)
             
    return maximo,minimo

def maximo(x,y,parte1,parte2):
    maximo,minimo=funcion(x,y,parte1,parte2)
    turtle.penup()
    turtle.goto(0,maximo*100)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.write(round(maximo,2),move=False, align="left", font=("Arial", 15, "normal"))
    turtle.penup()
    turtle.goto(0,minimo*100)
    turtle.pendown()
    turtle.write(round(minimo,2),move=False, align="left", font=("Arial", 15, "normal"))
    turtle.penup()
    turtle.home()
    turtle.pendown()
    






