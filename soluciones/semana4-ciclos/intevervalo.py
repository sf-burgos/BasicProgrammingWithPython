from sys import stdin
n=(stdin.readline().split())
def intervalo(n):
    pp=[]
    pp=[int(i) for i in n]
    if len(pp)==1 or len(pp)>=1000:
        print("No hay viaje!")
    else:
        print (min(pp),max(pp))

intervalo(n)
