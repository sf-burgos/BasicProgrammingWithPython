from sys import stdin


def crearMatriz(f,c):
    """
    PRE:
    POS:
    """
    mat = []
    for i in range(f):
        filas = []
        for j in range(c):
            filas.append(0)

        mat.append(filas)

    return mat

def sumarMat(m1,m2):
    """
    PRE:
    POS:
    """
    nf = len(m1)
    nc = len(m1[0])
    ms = crearMatriz(nf,nc)
    
    for i in range(nf):
        for j in range(nc):
            ms[i][j]=m1[i][j]+m2[i][j]

    return ms

def leerMat2():
    linea = stdin.readline().strip().split(",")
    nf1, nc1 = int(linea[0]),int(linea[1])
    mat1 = []
    #iterar sobre la cantidad de filas de la matriz1
    for m1 in range(nf1):
        #Convierto a lista de cadena cada una de las filas
        fila = [int(xx) for xx in stdin.readline().strip().split(",")]
        mat1.append(fila)

    return mat1


def leerMat():
    linea = stdin.readline().strip().split(",")
    nf1, nc1 = int(linea[0]),int(linea[1])
    mat1 = []
    #iterar sobre la cantidad de filas de la matriz1
    for m1 in range(nf1):
        #Convierto a lista de cadena cada una de las filas
        fila = stdin.readline().strip().split(",")
        #Recorro la lista de cadena para convertir a entero
        for i in range(nc1):
            fila[i]=int(fila[i])

        mat1.append(fila)

    return mat1

def validarTams(m1,m2):
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        return True
    else:
        return False
    

def main():
    m1 = leerMat2()
    m2 = leerMat2()

    if validarTams(m1,m2):
        print(sumarMat(m1,m2))
    else:
        print("No es Posible")
        
main()

    
