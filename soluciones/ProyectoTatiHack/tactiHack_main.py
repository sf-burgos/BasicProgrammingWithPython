from sys import stdin
import turtle
import random
from formaciones import *
from CampNou import *
from movimientos import *
from Registro import *
def main(n):
    opciones=["4-2-2","4-3-1-2","4-4-3","4-2-3-1","4-4-1-1","4-3-2-1","4-5-1","3-5-2","3-4-3","5-4-1","5-3-2","ingresar o alterar la alineacion predeterminada de tu equipo","usar SolvingHack"]
    #False: RED
    #True: Black 
    #F4_2_2(False)
    #F4_2_2(True)
    #F4_3_1_2(True)
    #F4_3_1_2(False)
    #F4_3_3(True)
    #F4_3_3(False)
    #F4_2_3_1(True)
    #F4_2_3_1(False)
    #F4_4_1_1(True)
    #F4_4_1_1(False)
    #F4_5_1(True)
    #F4_5_1(False)
    #F4_3_2_1(True)
    #F4_3_2_1(False)
    #F3_5_2(True)
    #F3_5_2(False)
    #F3_4_3(True)
    #F3_4_3(False)
    #F5_4_1(True)
    #F5_4_1(False)
    ##F5_3_2(True)
    #F5_3_2(False)
    if n==0:
        x=registro()
    else:
        print("Bienvenido a TATIHACK, porfavor ingrese el numero correspondiente a alineacion que quiere estudiar:")
        for i in range(len(opciones)):
            print(str(i+1)+str("/"),opciones[i])
        n=int(stdin.readline().strip())

        camp()
        if n==1:
            F4_2_2(True)
            F4_5_1(False)
            comentarios(1)
            #F3_5_2(False)
        elif n==2:
            F4_3_1_2(True)
            F5_3_2(False)
            comentarios(2)
            #
        elif n==3:
            F4_3_3(True)
            F5_3_2(False)
            comentarios(3)
            #F4_4_1_1(False)
        elif n==4:
            F4_2_3_1(True)
            F5_3_2(False)
            comentarios(4)
            #F4_4_1_1(False)
        elif n==5:
            F4_4_1_1(True)
            F3_4_3(False)
            comentarios(5)
            #F4_3_1_2(False)
        elif n==6:
            F4_3_2_1(True)
            F5_3_2(False)
            comentarios(6)
            #
        elif n==7:
            F4_5_1(True)
            F4_3_3(False)
            comentarios(7)
            #F4_2_2(False)
        elif n==8:
            F3_5_2(True)
            #F4_3_2_1(False)
            F5_3_2(False)
            comentarios(8)
            
        elif n==9:
            F3_4_3(True)
            F4_3_3(False)
            #F4_2_2(False)
            comentarios(9)
        elif n==10:
            F5_4_1(True)
            F4_5_1(False)
            comentarios(10)
            #F4_4_1_1(False)
        elif n==11:
            F5_3_2(True)
            F3_5_2(False)
            comentarios(11)
            #F4_3_2_1(False)
        elif n==12:
            numerodealineacion(x)
        elif n==13:
            pass
        else:
            print("Opcion incorrecta, intentelo de nuevo")



def comentarios(n):
    file= open("zcomentarios"+str(n)+".txt","r")
    a=file.read()
    turtle.goto(0,500)
    turtle.pencolor("White")
    turtle.write(a, move=True, align="center", font=("Cooper black", 12, "normal"))
    file.close()



def numerodealineacion(nombre):
    opciones=["4-2-2","4-3-1-2","4-4-3","4-2-3-1","4-4-1-1","4-3-2-1","4-5-1","3-5-2","3-4-3","5-4-1","5-3-2"]
    z=input("Desea ingresar o alterar la alineacion a su cuenta como predeterminada 1=Si-2=no")
    
    if z=="1":
        print("elija las opciones")
        for i in range(len(opciones)):
            print(str(i+1)+str("/"),opciones[i])

        alineacion=input("elija un numero de la alineacion")
        print(alineacion)
        c=open(str(nombre)+str("ali.txt"),"w")
        c.write(alineacion+"\n")
        c.close()
        main(1)
    if z==2:
        return
    else:
        print("opcion incorrecta")
        numerodealineacion(nombre)

        
main(0)
