from sys import stdin

def pan():
    m=int(stdin.readline().strip())
    lista=str(stdin.readline().strip())
    lista=lista.lower()
    lista2=[]
    comparacion=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in lista:
        lista2.append(i)
    orden=mergeSort(lista2)
    lista_nueva = []
    for i in orden:
         if i not in lista_nueva:
             lista_nueva.append(i)
    if lista_nueva==comparacion:
        print("YES")
    else:
        print("NO")
def mergeSort(lista):
    if len(lista)==1: return lista
    izq, der = dividirAlMedio(lista)
    lista1=mergeSort(izq)
    lista2=mergeSort(der)
    return merge(lista1,lista2)

def dividirAlMedio(lista):
    middle = len(lista) // 2
    return lista[0:middle], lista[middle:]
def merge(first, second):
    mergedList = []
    i, j = 0, 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            mergedList.append(first[i])
            i+=1
        else:
            mergedList.append(second[j])
            j += 1 
    mergedList.extend(first[i:])
    mergedList.extend(second[j:])
    return mergedList
pan()

