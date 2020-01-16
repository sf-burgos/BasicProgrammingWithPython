from sys import stdin
def criba_eratostenes(n):
        global lista
        multiplos = set()
        lista=[]
        for i in range(2, n+1):
                if i not in multiplos:
                        lista.append(i)
                        multiplos.update(range(i*i, n+1, i))
        return lista

def main():
        global lista2
        lista2=[]
        n=str(stdin.readline().strip())
        lista=criba_eratostenes(10000000)
        while n!="":
                n=int(n)
                print(salida(lista,n))
                n=str(stdin.readline().strip())
                
                
        





def salida(lista,n):
        circular=0


        for i in range(len(lista)):
                if i>n:
                        break
                else:
                        a=str(i)
                        if len(a)==1:
                                if i in lista:
                                        circular+=i
                                        

                        else:
                                if i not in lista2:
                                        for j in range(len(a)):
                                                
                                                a=a[1:]+a[0]
                
                                                if int(a) in lista:
                                                        t=True 
                                                else:
                                                        t=False
                                                        break
                                        if t:
                                                circular+=i
                                                lista2.append(i)
                                else:
                                        circular+=i
                                
        return circular

main()
