from sys import stdin    





def primerasdos():
    n=int(stdin.readline().strip())
    while n!=0:
        m=(stdin.readline().strip().split(" "))
        z=m[0]
        z=int(z)
        y=m[1]
        y=int(y)
        lista=[]
        filas=[]
        for i in range (y):
            filas.append(0)
        for j in range(z):
            lista.append(filas)       
            print (lista)
        n-=1
def main():
    primerasdos()
    

main()
