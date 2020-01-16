from sys import stdin

def main():
    n=[int(x)for x in stdin.readline().strip().split()]
    while n!=[0,0]:
        a=n[0]
        b=n[1]
        lista_numeros=[]
        for i in range(a,b+1):
            lista_numeros.append(i)
        lista_variables=[]
        for i in lista_numeros:
            
            lista=[]
            while i!=1:
                if i%2==0:
                    i=i/2
                    lista.append(int(i))
                elif i%2!=0:
                    i=(i*3)+1
                    lista.append(int(i))
            longitud=len(lista)
            lista_variables.append(longitud)
        print(a,b,max(lista_variables)+1)
        n=[int(x)for x in stdin.readline().strip().split()]
    

    

main()
