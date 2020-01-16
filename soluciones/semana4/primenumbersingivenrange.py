from sys import stdin
def main():
    entrada=[int(xx)for xx in stdin.readline().strip().split(" ")]
    x=entrada[0]
    y=entrada[1]
    for i in range(x,y+1):
        if es_primo(i):
            print(i)
def es_primo(x): #funcion es_primo(x) tomado de http://www.lawebdelprogramador.com/codigo/Python/2413-Determinar-si-un-numero-es-primo-o-no.html
    if x<2:
        return False 
    elif x==2:
        return True
    else:
        for n in range(2,x):
            if x%n == 0:
                return False
            elif(n == x-1):
                return True
main()
