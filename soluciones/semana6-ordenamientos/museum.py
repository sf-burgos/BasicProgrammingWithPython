from sys import stdin
def reloj():
    entrada=str(stdin.readline().strip())
    contador=0
    entrega=""
    inicio=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    inicioreverse=inicio[::-1]
    x=busqueda(inicio,i)
    y=busqueda(inicioreverse,i)
    lista1=inicio.copy()
    lista2=inicioreverse.copy()
    for i in entrada:
        if x>y:
            entrega=entrega+str(x+1)
            lista1=lista1
def busqueda(lista,x):
    i=0
    flag=-1
    for z in lista:
        if z ==x:
            flag=i
        i=i+1
    return flag
reloj()
#lista2=lista1[::-1]""reverse""____lista1=lista1+lista1[0::y]
