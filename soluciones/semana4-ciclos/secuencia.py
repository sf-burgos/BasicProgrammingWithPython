from sys import stdin
n=int(stdin.readline())


def iteracion1 (entrada):
        cont=0
        for i in range (0,n):
            cont=cont+2    
            multi=2**i    
            y=str(cont)
            print ((y*multi))

iteracion1 (n)
