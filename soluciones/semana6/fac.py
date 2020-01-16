from sys import stdin
from math import *

def main():
    n=(stdin.readline().strip())
    while n!="":
        n=int(n)

        
    
                
        lista=[40320,5040,720,120,24,6,2,1,1]
        cont=0
        pos=0
        result=0
        pot(lista,cont,pos,n,result)
        n=(stdin.readline().strip())
    
def pot(lista,cont,pos,n,result):
    if result==n:
        print(cont)
        return 
    else:
        if pos>=len(lista):
            print( cont)
            return
        if result+lista[pos]<=n:
            result+=lista[pos]
            cont+=1
            pot(lista,cont,pos,n,result)
        else:
            pot(lista,cont,pos+1,n,result)
            
                      
main()
