"""credito a: http://interactivepython.org/courselib/static/pythonds/SortSearch/TheBubbleSort.html"""
from sys import stdin
r=(stdin.readline().strip())
alist=[]
while r!="":
    alist.append(r)
    r=(stdin.readline().strip())
def bubbleSort(alist):
    contador =0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                contador+=1
    print(contador)

    
    
		
bubbleSort(alist)
print(alist)

