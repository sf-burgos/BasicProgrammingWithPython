from sys import stdin
import math

#area de circulos
def AreaC (radio):
    rta = math.pi*radio**2
    return rta

#area de cuadrado
def AreaL (Lado,radio):
    rta2 =(Lado+2*radio)**2
    return rta2

def principal ():

    R= float(stdin.readline().strip())        
    r= float(stdin.readline().strip())
    L= float(stdin.readline().strip())
    if R<=0 or r<=0 or L<=0:
        print ("Datos Erroneos")
    else:
        a= AreaC(R)
        b= AreaC(r)
        c= AreaL(L,r)
        d= c-(b+a)
        d= round(d,2)
        print ("El area es:",d)
principal()


