import turtle



def dib_espiral(tortuga,longitud, grosor,color, con):
    """PRE: Sus parametros son: la variable es tipo tortuga, la longitud
    a la cual se le restara -5 de forma recurrente, el grosor de la tortuga,
    el color que tendra y un contador (con) que permite cambiar el color
    tambien de forma recurrente
    POS: la funcion permite dibujar un pentagono, hasta que la longitud sea 0
    """
  
    tortuga.speed(1000)
    if con==4:
        con=1
    if longitud > 0 and grosor > 0:
        tortuga.pensize(grosor)
        tortuga.forward(longitud)
        tortuga.right(72)
        colora=color123(con)
        tortuga.color(color)
        con=con+1
        dib_espiral(tortuga,longitud-5, grosor-0.3, colora, con)
def color123 (con):
    """ PRE: sus argumentos son: el contador (con) que de forma recurrente retorna
    un valor a la tortuga"
    POS: cambiar el color depende de del (con) y cuando con==4, lo reinicia y lo
    vuelve con=1 para iniciar de nuevo"""
    if con==1:
         return "black"
    elif con==2:
        return "blue"
    elif con==3:
        return "red"
    """
    PRE: Ninguna
    POS: llama la funcion dib_espiral con la tortuga, la longitud, el grosor, el
    color inicial de la funcion y el valor del contador"""

def main():
    tt = turtle.Turtle()
    dib_espiral(tt,200, 16,"black",1)

main()
