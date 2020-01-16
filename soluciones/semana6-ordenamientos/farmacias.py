from sys import stdin
def main():
    n=int(stdin.readline().strip())
    lista=str(stdin.readline().strip())
    while lista!="0":
        busquedalinealZ(lista)
        n=int(stdin.readline().strip())
        lista=str(stdin.readline().strip())

def busquedalinealZ (lista):
    lista2=[]
    p=0
    comodin=-1
    p2=0
    comodin2=-1
    for i in lista:
        lista2.append(i)
    if "Z" in lista2:
        print(0)
    else:
        for i in lista2:
            if i=="R":
                comodin=p
            p=p+1
            if i=="D":
                comodin2=p2
            p2=p2+1
        print(abs (comodin-comodin2))

main()
