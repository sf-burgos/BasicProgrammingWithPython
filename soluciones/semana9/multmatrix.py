from sys import stdin
def crearMatriz(f,c): 
    mat = []
    for i in range(f):
        filas = []
        for j in range(c):
            filas.append(0)

        mat.append(filas)

    return mat
def matiz(filas,columnas,lista):
    cont=0
    mat=[]
    for i in range(filas):
        filas=[]
        for j in range(columnas):
            
            filas.append(lista[cont])
            cont+=1
        mat.append(filas)

    return mat
def multmat(f1,c2,f2,lista,m1,m2):
    for r in range(0,f1):
        for c in range(0,c2):
            for k in range(0,f2):
                lista[r][c]+=m1[r][k]*m2[k][c]
    return lista


def main():
    longitud=[int(x)for x in stdin.readline().strip().split(",")]
    entrada1=[int(x) for x in stdin.readline().strip().split(",")]
    longitud2=[int(x)for x in stdin.readline().strip().split(",")]
    entrada2=[int(x) for x in stdin.readline().strip().split(",")]
    
    if longitud[1]!=longitud2[0]:
        print("Impossible")
        return

    else:




        
        matriz_sola=crearMatriz(longitud[0],longitud2[1])
        matriz1=matiz(longitud[0],longitud[1],entrada1)
        matriz2=matiz(longitud2[0],longitud2[1],entrada2)
        salida=multmat(longitud[0],longitud2[1],longitud2[0],matriz_sola,matriz1,matriz2)
        for i in salida:
            x=list(i)
            print(*x)
        





main()
