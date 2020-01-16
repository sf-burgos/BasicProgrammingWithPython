import turtle
import random
def dib_arbol(lon_rama,tortu):
   if lon_rama > 5:
       tortu.fd(lon_rama)
       tortu.rt(20)
       dib_arbol(lon_rama-12,tortu)
       tortu.lt(40)
       dib_arbol(lon_rama-12,tortu)
       tortu.rt(20)
       tortu.bk(lon_rama)  
def main():
   n=int(input("ìngrese el n que desea para verificar el programa "))
   t= turtle.Turtle()
   t.lt(90)
   dib_arbol((n*10)+10,t)
main()
