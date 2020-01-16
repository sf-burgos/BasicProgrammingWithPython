from sys import stdin
import turtle
import math
def entrada():
    lista=[str(arr_temp) for arr_temp in stdin.readline().strip().split(" ")]
    amplitud=int(lista[0])
    funcion=lista[1]
    variable=(lista[2])
    variable=variable.replace("(","")
    reflexionx=lista[3]
    corrimientox=str(lista[4])
    corrimientox=corrimientox.replace(")","")
    corrimientox=int(corrimientox)
    reflexiony=lista[5]
    corrimientoy=int(lista[6])
    return lista,amplitud,funcion,variable,reflexionx,corrimientox,reflexiony,corrimientoy

