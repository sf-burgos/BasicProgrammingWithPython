import turtle
import random

def calidad (lon):
    """PRE: su unico parametro es el radio del circulo, ademas de ser tipo tortuga.
    POS: permite dibujar circulos de diferentes tamaños,
    partiendo siempre desde el mismo punto"""
    if lon>0:
        turtle.speed()
        pos=ale()
        turtle.color(pos)
        turtle.begin_fill()
        turtle.circle(lon)
        turtle.end_fill()

        calidad(lon-10)
    """PRE: ninguno
    POS: cambia el color aleatoriamente por medio de la libreria "import random",
    por medio de la escala de colores RGB"""
        
def ale():
    r=random.random()
    g=random.random()
    b=random.random()
    return (r,g,b)

calidad(70)
    
