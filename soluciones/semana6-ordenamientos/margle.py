from sys import stdin

def main ():
    lista=[int(arr_temp) for arr_temp in stdin.readline().strip().split(" ")]
    x=lista[0]
    y=lista[1]
    casos=1
    while x!=0 and y!=0:
        alist=[]
        while x!=0:
            n=int(stdin.readline().strip())
            alist.append(n)
            x-=1
        busqueda=[]
        while y!=0:
            m=int(stdin.readline().strip())
            busqueda.append(m)
            y-=1
        alist=(mergeSort(alist))
        print("CASE#",str(casos)+":")
        
        for i in busqueda:
            m=busquedauni(alist,i)+1
            if m==0:
                print(str(i),"not found")
                
            else:
                print(str(i),str("found at"),str(m))
                
        lista=[int(arr_temp) for arr_temp in stdin.readline().strip().split(" ")]
        x=lista[0]
        y=lista[1]
        casos=casos+1
           

##    (mergeSort(alist))#listaordenada
#ordenar (lista)
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return alist

def busquedauni(lista,x):
    i=0
    flag=-1
    for z in lista:
        if z ==x:
            flag=i
            return flag
        i=i+1
    return flag
    

main()
