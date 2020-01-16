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
    turtle.screensize(x,y)
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(1000,0)
    turtle.pendown()

    '''    if 'pi' in parte1:
        parte1=parte1.replace('pi','pi*10')

   ''' 

    if '1/sen' in parte1 or '1/tan' in parte1:
        lista=[]
        for i in range(-1000,1000,25):
            lista.append(i)
        lista.remove(0)
        for i in lista:
            if i==1:
                turtle.penup()
                turtle.goto(-1,0)
                turtle.pendown()
            else:
                turtle.pencolor('green')
                y=eval(str(parte1)+str(i)+str(parte2))
                turtle.goto(i*-1,100*y)
    

    else:
        for i in range(-1000,1000,25):
                turtle.pencolor('green')
                y=eval(str(parte1)+str(i)+str(parte2))
                turtle.goto(i*-1,100*y)
                
            
    turtle.penup()
    turtle.home()
    turtle.pendown()  


        



