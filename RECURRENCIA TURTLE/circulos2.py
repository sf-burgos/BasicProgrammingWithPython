import turtle
"""PRE: sus parametros son la longitud(lon) del tortuga y el grosor(groz) del pincel.
POS:dibuja circulos de diferentes tamaños hacia el centro de forma recurrente"""
def calidad (lon,groz):
    if lon>0:
        turtle.speed(500)
        turtle.pensize(groz)
        turtle.circle(lon)
        turtle.lt(90)
        turtle.pu()
        turtle.fd(10)
        turtle.rt (90)
        turtle.pd()
        calidad(lon-10, groz)

calidad(200,5)
