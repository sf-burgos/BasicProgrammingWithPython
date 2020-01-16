"""credito a: http://interactivepython.org/courselib/static/pythonds/SortSearch/TheBubbleSort.html"""
from sys import stdin
def main():
    n=int(stdin.readline().strip())
    alist=[]
    while n!=0:
        while n!=0:
            m=int(stdin.readline().strip())
            alist.append(m)
            n-=1
        n=int(stdin.readline().strip())
        r=bubbleSort(alist)
        print(r)
        alist=[]

def bubbleSort(alist):
    contador=0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                contador+=1
    return contador #usa el contador de la funcion burble  
            

        
main()
