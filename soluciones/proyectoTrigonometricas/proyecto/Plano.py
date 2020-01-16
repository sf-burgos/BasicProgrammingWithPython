import turtle
""" Pre: ninguna()
Pos: por medio de la libreria turtle, dibujara un plano cartesiano,pondra titulo a la
ventana y cambiara el color"""
def completo():
    turtle.screensize(10000000,10000000)
    wn=turtle.Screen()#llamamos a la funcion de la ventana
    wn.bgcolor('#01F8FF')#damos un color a la ventana 
    wn.title("Funciones Trigonometricas")#nombre del proyecto 
    t=turtle#inicio del plano cartesiano 
    turtle.speed(100)#tiene un limite, tal vez suficiente para millones de funciones trigonometricas
    turtle.pencolor("black")
    turtle.rt(90)
    turtle.pensize(3)
    turtle.goto(0,0)
    turtle.rt(90)
    turtle.fd(100000)
    turtle.goto(0,0)
    turtle.rt(90)
    turtle.fd(100000)
    turtle.goto(0,0)
    turtle.rt(90)
    turtle.fd(100000)
    turtle.fd(100000)
    turtle.goto(0,0)
    turtle.rt(90)
    turtle.fd(100000)
    turtle.pu()
    '''t.goto(0,0)
    t.rt(270)#final del plano cartesiano
    t.pd()
    '''


    

