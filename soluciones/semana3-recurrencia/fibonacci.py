from sys import stdin
p=int(stdin.readline())
"""PRE:Fibonacci consiste en la ecuacion de recurrencia ((an-1)*3)+(an-2)-(an-3)
necesita una entrada de un entero"""
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
