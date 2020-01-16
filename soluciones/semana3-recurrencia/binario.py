
from sys import stdin
"""pasa todos los numeros al sistema hexagecimal"""
def binarios(f,cadena,pot):
    if f>0:
        a=(f%2)*(2)**pot
        pot=pot+1
        cadena=str(a)+" "+cadena
        x= binarios(int(f/2),cadena,pot)  
    
    else:
         print (cadena)

def main():
    f=int(stdin.readline().strip())
    cadena= ""
    if f==0:
        print(0)
    else:    
        binarios(f,cadena,0)     
main()      
