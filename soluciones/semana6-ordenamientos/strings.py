from sys import stdin
def reducir():
    n = str(stdin.readline().strip())
    lista = []
    for i in range(len(n)):
        if not lista or n[i] != lista[-1]:
            lista += [n[i]]
        else:
            lista.pop()
    if lista:
        print (''.join(lista))
    else:
        print ('empty String')
reducir()
