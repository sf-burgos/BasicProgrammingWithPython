from sys import stdin
#1000 2000 3000


def valdez(n):
    z=max(n)
    y=min(n)
    n.remove(y)
    n.remove(z)
    p=n[0]
    return p

def main():
    o=int(stdin.readline())
    c=1
    for i in range (o):
        n= [int(xx) for xx in stdin.readline().strip().split(' ')]
        print("Case",str(c)+":",valdez(n))
        c+=1
main()

