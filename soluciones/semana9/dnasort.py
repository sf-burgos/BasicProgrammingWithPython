from sys import stdin
def quickSort(alist):
    #Pre: Una lista ordenable
    #pos: Una lista ordenada """
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    #pre: una lista ordenable,con un pivote y una lista de salida
     #returnara un marcador derecho o pivote """ 
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark
def bubbleSort(alist,listanumeros,listagrande):
    cont=0
    alist=list(alist)
    alist2=alist.copy()
    a=""
    for i in range(len(alist2)):
        a+=alist[i]
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                cont+=1

    listanumeros.append(cont)
    listagrande.append(cont)
    listagrande.append(a)
def main():
 
    n=int(stdin.readline().strip())
    for j in range(n):
        k=str(stdin.readline().strip())
        listanumeros=[]
        listagrande=[]
        datos=[int(s) for s in stdin.readline().strip().split(" ")]
        cont=0
        for i in  range(datos[1]):
            alist =str(stdin.readline().strip())
            bubbleSort(alist,listanumeros,listagrande)

            quickSort(listanumeros)

        for i in range(len(listagrande)):
            a=listagrande.index(listanumeros[cont])
            listagrande[a]=-1
            print(listagrande[a+1])
            if cont==len(listanumeros)-1:
                break
            else:
                cont+=1
        if j<n-1:
           print()
     
main()

