from sys import stdin
def impar(n,m):
    z=int()
    numimpares=int()
    for impares in range (n,m+1):
        if impares%2==0:
            z+=impares
        else:
            numimpares+=impares
    return (numimpares)
    
def main():
    z=int(stdin.readline())
    c=1
    for i in  range (z):
        n=int(stdin.readline().strip())
        m=int(stdin.readline().strip())
        impar(n,m)
        print("Case",str(c)+":",impar(n,m))
        c+=1
main()
