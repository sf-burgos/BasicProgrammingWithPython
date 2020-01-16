""" credito a: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html"""
from sys import stdin 
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
def main():
    n=int(stdin.readline().strip())
    alist=[int(arr_temp) for arr_temp in stdin.readline().strip().split(" ")]
    insertionSort(alist)
    suma=0
    c=-1
    x=0
    while suma<n:
        suma+=alist[c]
        c-=1
        x+=1
    print(x)
main()
