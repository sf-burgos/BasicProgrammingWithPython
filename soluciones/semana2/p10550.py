from sys import stdin
def main():
    lista=[]
    for i in range (4):
        a=str(stdin.readline().strip())
        lista.append(a)
    

    degree=120
    degree+=(int(lista[0]) - int(lista[1]) + 40) % 40
    degree += (int(lista[2]) - int(lista[1]) + 40) % 40
    degree += (int(lista[2]) - int(lista[3]) + 40) % 40

    print(degree*9)
main()
