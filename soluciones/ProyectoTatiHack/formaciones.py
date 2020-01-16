from sys import stdin
import turtle
import random
t=turtle
"""https://listas.20minutos.es/deportes/las-mejores-formaciones-del-futbol-414044/"""#imagenes de las formaciones
"""https://trucosytips.wordpress.com/2008/01/26/toda-enfermedad-tiene-su-remedio/"""#formaciones contrarestantes
#FORMACIONES
def F4_2_2(lado):
    Arquero(lado)
    Defensa4(lado)
    Medio4(lado)
    Delantera2(lado)
def F4_3_1_2(lado):
    Arquero(lado)
    Defensa4(lado)
    Medio3(lado)
    Delantera1_2(lado)
def F4_3_3(lado):
    Arquero(lado)
    Defensa4(lado)
    Medio3(lado)
    Delantera3(lado)
def F4_2_3_1(lado):
    Arquero(lado)
    Defensa4(lado)
    Medio2_3(lado)
    Delantera1(lado)
def F4_4_1_1(lado):
    Arquero(lado)
    Defensa4(lado)
    Medio4(lado)
    Delantera1(lado)
    if lado:
        t.goto(-90,-10)
        jugador("black")
    else:
        t.goto(90,-10)
        jugador("red")
def F4_3_2_1(lado):
    Arquero(lado)
    Defensa4(lado)
    Medio3(lado)
    Delantera2_1(lado)
def F4_5_1(lado):
    Arquero(lado)
    Defensa4(lado)
    Medio5(lado)
    Delantera1(lado)

    
def F3_5_2(lado):
    Arquero(lado)
    Defensa3(lado)
    Medio5(lado)
    Delantera2(lado)
def F3_4_3(lado):
    Arquero(lado)
    Defensa3(lado)
    Medio4(lado)
    Delantera3(lado)
def F5_4_1(lado):
    Arquero(lado)
    Defensa5(lado)
    Medio4(lado)
    Delantera1(lado)
def F5_3_2(lado):
    Arquero(lado)
    Defensa5(lado)
    Medio3(lado)
    Delantera2(lado)


    



    

    
    
    
    
    

    

        
    
#Funciones Alternas
#___________________________________________________________________________________________________________________________________
def Arquero(lado):
    """pre: necesidad del lado  1=izquierdo, 2=derecho"""
    #t.pencolor("black")
    #t.color("black")
    if lado:
        t.goto(-500,-20)
        jugador("black")
        
        
        
    else:
        t.goto(500,-20)
        jugador("red")
def Defensa4(lado):
    if lado:
        t.goto(-330,-60)
        jugador("black")
        t.goto(-330,60)
        jugador("black")
        t.goto(-280,200)
        jugador("black")
        t.goto(-280,-200)
        jugador("black")
        
    else:
        t.goto(330,-60)
        jugador("red")
        t.goto(330,60)
        jugador("red")
        t.goto(280,200)
        jugador("red")
        t.goto(280,-200)
        jugador("red")
def Defensa3(lado):
    if lado:
        t.goto(-330,0)
        jugador("black")
        t.goto(-330,100)
        jugador("black")
        t.goto(-330,-100)
        jugador("black")
    else:
        t.goto(330,0)
        jugador("red")
        t.goto(330,100)
        jugador("red")
        t.goto(330,-100)
        jugador("red")
def Defensa5(lado):
    if lado:
        t.goto(-330,0)
        jugador("black")
        t.goto(-330,100)
        jugador("black")
        t.goto(-330,-100)
        jugador("black")
        t.goto(-250,200)
        jugador("black")
        t.goto(-250,-200)
        jugador("black")
    else:
        t.goto(330,0)
        jugador("red")
        t.goto(330,100)
        jugador("red")
        t.goto(330,-100)
        jugador("red")
        t.goto(250,200)
        jugador("red")
        t.goto(250,-200)
        jugador("red")

def Medio4(lado):
    if lado:
        t.goto(-170,-60)
        jugador("black")
        t.goto(-170,60)
        jugador("black")
        t.goto(-120,200)
        jugador("black")
        t.goto(-120,-200)
        jugador("black")
        
    else:
        t.goto(170,-60)
        jugador("red")
        t.goto(170,60)
        jugador("red")
        t.goto(120,200)
        jugador("red")
        t.goto(120,-200)
        jugador("red")
def Medio3(lado):
    if lado:
        t.goto(-190,0)
        jugador("black")
        t.goto(-190,100)
        jugador("black")
        t.goto(-190,-100)
        jugador("black")
    else:
        t.goto(190,0)
        jugador("red")
        t.goto(190,100)
        jugador("red")
        t.goto(190,-100)
        jugador("red")
def Medio2_3(lado):
    if lado:
        t.goto(-220,-100)
        jugador("black")
        t.goto(-220,70)
        jugador("black")
        #
        t.goto(-120,0)
        jugador("black")
        t.goto(-120,100)
        jugador("black")
        t.goto(-120,-100)
        jugador("black")
        

        
    else:
        t.goto(220,-100)
        jugador("red")
        t.goto(220,70)
        jugador("red")
        
        t.goto(120,0)
        jugador("red")
        t.goto(120,100)
        jugador("red")
        t.goto(120,-100)
        jugador("red")
def Medio5(lado):
    if lado:
        t.goto(-220,0)
        jugador("black")
        t.goto(-220,100)
        jugador("black")
        t.goto(-220,-100)
        jugador("black")
        t.goto(-160,200)
        jugador("black")
        t.goto(-160,-200)
        jugador("black")
    else:
        t.goto(220,0)
        jugador("red")
        t.goto(220,100)
        jugador("red")
        t.goto(220,-100)
        jugador("red")
        t.goto(160,200)
        jugador("red")
        t.goto(160,-200)
        jugador("red")


def Delantera1(lado):
    if lado:
        t.goto(-30,-10)
        jugador("black")
    else:
        t.goto(30,-10)
        jugador("red")

    
def Delantera2_1(lado):
    if lado:
        t.goto(-80,-100)
        jugador("black")
        t.goto(-80,70)
        jugador("black")
        t.goto(-30,-20)
        jugador("black")
    else:
        t.goto(80,-100)
        jugador("red")
        t.goto(80,70)
        jugador("red")
        t.goto(30,-20)
        jugador("red")
def Delantera1_2(lado):
    if lado:
        t.goto(-30,-100)
        jugador("black")
        t.goto(-30,70)
        jugador("black")
        t.goto(-100,-20)
        jugador("black")
    else:
        t.goto(30,-100)
        jugador("red")
        t.goto(30,70)
        jugador("red")
        t.goto(100,-20)
        jugador("red")
    
        
        
    
def Delantera2(lado):
    if lado:
        t.goto(-30,-100)
        jugador("black")
        t.goto(-30,70)
        jugador("black")
    else:
        t.goto(30,-100)
        jugador("red")
        t.goto(30,70)
        jugador("red")
def Delantera3(lado):
    if lado:
        t.goto(-50,0)
        jugador("black")
        t.goto(-50,100)
        jugador("black")
        t.goto(-50,-100)
        jugador("black")
    else:
        t.goto(50,0)
        jugador("red")
        t.goto(50,100)
        jugador("red")
        t.goto(50,-100)
        jugador("red")

    
        
def jugador(a):
    t.pd()
    t.color(a)
    t.begin_fill()
    t.circle(20)
    turtle.end_fill()
    t.pu()
    
