from sys import stdin


def numero (n):
    if n==1:
        return 1
    else:
        n=n+numero(n-1)
        return n
    

def main():
    n=int(stdin.readline())
    z= numero(n)
    print ("T("+str(n)+")="+str(z))
main()
