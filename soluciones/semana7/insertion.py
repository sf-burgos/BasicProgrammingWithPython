from sys import stdin
def insertionSort(alist):
    cont=0
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            cont+=1
            
        alist[position]=currentvalue
    return cont
      
def main():
    n=int(stdin.readline().strip())
    for i in range(n):
        lon=int(stdin.readline().strip())
        alist=[int(s)for s in stdin.readline().strip().split()]
        print(insertionSort(alist))

main()
