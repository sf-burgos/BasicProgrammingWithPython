import turtle

def dibLinea(nx,ny,leo,long):
    """
    PRE: Conocer valor de x y y, donde se desea hacer una recta. Además la
    variable tipo tortuga y la longitud de la recta.
    POS: Realiza una línea recta de tamaño long desde la posición nx y ny
"""
    leo.penup()
    leo.goto(nx,ny)
    leo.pendown()
    leo.fd(long)

def dibGrilla(leo):
    """
    PRE: La variable tipo tortuga
    POS: Reliza las cuatro líneas que componenen grilla
    dos horizontales y dos verticales
"""
    #Líneas horizontales
    dibLinea(0,0,leo,300)
    dibLinea(0,100,leo,300)

    #Líneas verticales
    leo.left(90)
    dibLinea(100,-100,leo,300)
    dibLinea(200,-100,leo,300)

def dibCirculo(nx,ny,leo,r):
    """
    PRE: Posición x y y del círculo, variable tipo tortuga y el
    valor del radio r del círculo
    POS: Círculo graficado en la posición indicada.
"""
    leo.penup()
    leo.goto(nx,ny)
    leo.pendown()
    leo.circle(r)

def dibEquis(nx,ny,leo,lado):
    """
    PRE: Conocer la posición, y el valor del lado de la X
    POS: Se realiza la grafica de X en la posición nx y ny
"""
    #Dibujar la linea /
    leo.rt(45)
    dibLinea(nx,ny,leo,lado)

    #Dibujar la linea \
    leo.rt(-90)
    dibLinea(nx+75,ny,leo,lado)

    #Volver a dejar la tortuna en posición original.
    leo.rt(45)

def main():
    """
    PRE: ninguna
    POS: Generá el tablero indicado.
"""
    ninja = turtle.Turtle()
    ninja.pensize(4)

    dibGrilla(ninja)
    #Dibujar los círculos
    dibCirculo(190,-45,ninja,40)
    dibCirculo(290,-45,ninja,40)

    #Dibujar las tres equis X
    dibEquis(10,-95,ninja,110)
    dibEquis(110,5,ninja,110)
    dibEquis(210,105,ninja,110)


main()
    
