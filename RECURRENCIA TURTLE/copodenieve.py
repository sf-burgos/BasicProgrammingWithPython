import turtle
def nieve(con,avance20,giro):
    """ PRE: sus parametros son: un contador(con) que permite saber cuando
    cada parte del copo de nieve(7), el avance tipo tortuga hacia adelante y hacia
    atras, y el giro del copo en grados(55)
    POS: permite dibujar una de las ramas del copo de nieve
    """
    if con==7:
        con==0
    else:
        turtle.pensize(5)
        turtle.color("blue")
        turtle.lt(90)
        turtle.fd(30)
        turtle.rt(giro)
        turtle.fd(avance20)
        turtle.bk(avance20)
        turtle.lt(110)
        turtle.fd(avance20)
        turtle.bk(avance20)
        turtle.rt(giro)
        turtle.fd(avance20)
        turtle.rt(giro)
        turtle.fd(35)
        turtle.bk(35)
        turtle.lt(110)
        turtle.fd(35)
        turtle.bk(35)
        turtle.rt(giro)
        turtle.fd(avance20)
        turtle.rt(giro)
        turtle.fd(25)
        turtle.bk(25)
        turtle.lt(110)
        turtle.fd(25)
        turtle.bk(25)
        turtle.rt(giro)
        turtle.bk(70)
        turtle.lt(210)
        con=con+1
        nieve(con, avance20, giro)
def contador():
    """ PRE: NINGUNO
    POS: Contador permite que el programa termine cuando el copo sea igual a 0"""
    if con==1:
        return con+1
    elif con==2:
        return con+1
    elif con==3:
        return con+1
    elif con==4:
        return con+1
    elif con==5:
        return con+1
    elif con==6:
        return con+1
    elif con==7:
        return 0
    
def main():
    """PRE: NINGUNA
    POS: llama la funcion nieve y le pasa los tres parametros que necesita, sobre
    el mas importante es el contador en 1, ya que es el arranque del programa"""
    nieve(1,20, 55)
main()
