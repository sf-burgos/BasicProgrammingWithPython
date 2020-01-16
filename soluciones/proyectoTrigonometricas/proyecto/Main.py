from aseno import*
from bcoseno import*
from ctangente import*
from dsecante import*
from ecosecante import*
from fcotangente import*
from Plano import *
from xEntrada import *
from math import *
import turtle

"""Pre: ninguna
Pos: Llamara la entrada del programa y con ella graficara la funcion"""
def main():
    parte1,parte2=entrada()
  
    if 'sin' in parte1 or 'sen' in parte1:
        x=eval(str('2*pi')+str('*50'))
        y=100
        completo()
        maximo(x,y,parte1,parte2)
        
        
 
    elif 'cos' in parte1:
        x=eval(str('2*pi')+str('*50'))
        y=100
        completo()
        funcion(x,y,parte1,parte2)
        
    elif 'tan' in parte1:
        x=eval(str('2*pi')+str('*50'))
        y=100
        completo()
        funcion(x,y,parte1,parte2)

    elif '1/sin' in parte1:
        x=eval(str('2*pi')+str('*50'))
        y=100
        completo()
        funcion(x,y,parte1,parte2)
        
    elif '1/cos' in parte1:
        x=eval(str('2*pi')+str('*50'))
        y=100
        completo()
        funcion(x,y,parte1,parte2)
        
    elif '1/tan' in parte1:
        x=eval(str('2*pi')+str('*50'))
        y=100
        completo()
        funcion(x,y,parte1,parte2)
    
        
main()


        

    
    
