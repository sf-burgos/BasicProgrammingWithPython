"""credito a: http://interactivepython.org/courselib/static/pythonds/SortSearch/TheSelectionSort.html"""
from sys import stdin
l=int(stdin.readline().strip())
alist=[int(arr_temp) for arr_temp in stdin.readline().strip().split(" ")]
def selectionSort(alist):
         for fillslot in range(len(alist)-1,0,-1):
             positionOfMax=0
             for location in range(1,fillslot+1):
                 if alist[location]>alist[positionOfMax]:
                     positionOfMax = location

             temp = alist[fillslot]
             alist[fillslot] = alist[positionOfMax]
             alist[positionOfMax] = temp

      
selectionSort(alist)
alist=str(alist)
alist=alist.replace(",","")
alist=alist.replace("[","")
alist=alist.replace("]","")

print(alist)
