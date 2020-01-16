from sys import stdin
n=int(stdin.readline().strip())
alist=[int(arr_temp) for arr_temp in stdin.readline().strip().split(" ")]

def insertionSort(alist):
    """ Ordena lista mediante el metodo insertion sort
    Pre: lista debe contener elementos comparables.
    Devuelve: una nueva lista ordenada."""
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        #Desplazamiento de los elementos de la matriz
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
            b=''
            for i in alist:
                b=b+str(i)+str(" ")
            print(b)
        #insertar el elemento en su lugar
        alist[position]=currentvalue
    a=''
    for i in alist:
        a=a+str(i)+str(" ")
    print(a)
insertionSort(alist)       
