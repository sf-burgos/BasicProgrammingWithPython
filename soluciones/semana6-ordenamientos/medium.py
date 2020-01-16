from sys import stdin
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
def app(alist):
    alist=mergeSort(alist)
    if len(alist)==1:
        print (alist[0])
    elif len(alist)%2==0:
        z=len(alist)
        a=(z//2)
        b=(z//2)-1
        print((alist[a]+alist[b])//2)
    else:
        y=len(alist)//2
        print(alist[y])
def main():
    alist=[]
    n=(stdin.readline().strip())
    while n!="":
        n=int(n)
        alist.append(n)
        app(alist)
        n=(stdin.readline().strip())
main()
        
    
    
        
