from sys import stdin
a=int(stdin.readline())
def recu(a):
    if a==0 :
        return 0
    else:
        return a%10+recu(a//10)
print (recu(a))

