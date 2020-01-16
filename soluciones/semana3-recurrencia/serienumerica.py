from sys import stdin
p=int(stdin.readline())
def bio (n):
    if n==0:
        return 1
    if n==1:
        return 2
    if n==2:
        return 5
    else:
        return (bio(n-1)*3)+(bio(n-2)-bio(n-3))
print(bio(p))
