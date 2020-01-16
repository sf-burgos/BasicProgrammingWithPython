from sys import stdin

def calidad(lista,valor,z):
    if valor==0:
        z=z + ","+ str(lista[0]) 
        print (z[x:])

    else:
        z= z + ","+str(lista[valor])
        return calidad(lista,valor-1,z)
def main ():
    x = [int(arr_temp) for arr_temp in input().strip().split(',')]

    entrada= ""
    recur=(x,len(x)-1,entrada)

main()
