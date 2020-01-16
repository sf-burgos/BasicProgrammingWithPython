from sys import stdin
def main():
    n=int(stdin.readline().strip())
    martina=0
    benjamin=0
    empate=0
    for i in range(n):
        entradas=[int(c) for c in stdin.readline().strip().split()]
        entradas=entradas[1::]
        a=entradas.count(0)
        b=entradas.count(1)
        if a>b:
            martina+=1
        elif b>a:
            benjamin+=1
        else:
            empate+=1
    print(martina,benjamin,empate)

main()
