from sys import stdin

def main():
    n=int(stdin.readline().strip())
    if 1<=n<=10**3:
        lista=[1,2]
        z=10**3
        for i in range(1,z+1):
            lista.append(1+lista[int(i)+1-lista[lista[int(i)-1]]])
        while n!=0:
            print(a(n,lista))
            n=int(input())
              
def a(n,lista):
    if n==1:
        return 1 
    elif n==2:
        return 2 
    elif n==3:
        return 2  
    else:
        return  lista[n]



main()
