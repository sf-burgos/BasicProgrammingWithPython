from sys import stdin

def main():
    n=[int(xx)for xx in stdin.readline().strip().split(",")]
    m=[int(xx)for xx in stdin.readline().strip().split(",")]
    lista=[]
    (pot(n,m,0,lista))
    lista.sort()
    print(lista)
    
    
def pot(n,m,cont,lista):
    if cont==len(n)-1:
        return lista#caso base
    else:
        x=n[cont]
        y=m[cont]
        z=x**y
        lista.append(round(z,1))
    pot(n,m,cont+1,lista)

#-3,2,-1,5,-2,0
#2,-1,-2,3,1,4
main()
