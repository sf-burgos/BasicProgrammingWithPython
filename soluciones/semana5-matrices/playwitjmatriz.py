from sys import stdin

#row a b, se cambia la fila a,b
#def row():
#col a b,se cambia la columna a por la b
#def cola():

#inc,sumar 1 a cada celda, si es 10, cambiar por 0
#def inc():
#dec, restar 1 a cada celda, si es -1, camviar por 9
#def dec:

def main():
#entrada con numero de casos; matriz de n*n(menor a 10)
    n=int(stdin.readline().strip())
    m=int(stdin.readline().strip())
    k=[]
    
    while m>0:
        matriz=[int(x) for x in stdin.readline().strip().split()]
        matriz=str(matriz)
        for ii in matriz:
            k+=ii
            m-=1
    print(k.replace(" ",""))
        #ESE UNO PA QUE
    tipo=str(stdin.readline().strip())
main()
    
