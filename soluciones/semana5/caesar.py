from sys import stdin
def main():
    n=int(stdin.readline().strip())
    for j in range(n):
        palabra=str(stdin.readline().strip())
        cont=int(stdin.readline().strip())
        letras="abcdefghijklmnopqrstuvwxyz"
        letras_2=letras.upper()
        hoy=""
        for i in palabra:
            if i in letras:
                indice=letras.index(str(i))
                x=((indice)+cont)%26
                hoy+=str(letras[x])
            elif i in letras_2:
                indice=letras_2.index(str(i))
                x=((indice)+cont)%26
                hoy+=str(letras_2[x])
            else:
                hoy+=i
        print("Case"+str(j+1),"=",hoy)
main()


