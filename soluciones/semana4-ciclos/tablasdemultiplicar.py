from sys import stdin
def multi(a):
    for numero in range(1,10):
        print(str(a)+"X"+str(numero)+"="+str(numero*a))
    
def main():
    rta=int(stdin.readline())
    multi(rta)
main()    
