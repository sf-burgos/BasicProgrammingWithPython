from sys import stdin

def main():
    n=[int(xx)for xx in stdin.readline().strip().split(",")]
    m=[int(xx)for xx in stdin.readline().strip().split(",")]
    lista=[]
    (pot(n,m,0,lista))
    quickSort(lista)
    for i in range(len(lista)):
        lista[i]=str(lista[i])
        

    

    print(",".join(lista)) 
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
def pot(n,m,cont,lista):
    if cont==len(n):
        return lista#caso base
    else:
        x=n[cont]
        y=m[cont]
        z=x**y
        lista.append(round(z,1))
    pot(n,m,cont+1,lista)

#-3,2,-1,5,-2,0
#2,-1,-2,3,1,4
main()
