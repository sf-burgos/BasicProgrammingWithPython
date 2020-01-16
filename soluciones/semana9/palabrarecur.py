from sys import stdin
def main():
    n=str(stdin.readline().strip())
    
    while n!="":
        d=""
        (reverse(n,-1,d))
        n=str(stdin.readline().strip())
       


def reverse(n,cont,d):
    if cont==(len(n)+1)*-1:
        print(d)
        return d
        
    else:
        z=n[cont]
        d=d+str(z)
        reverse(n,cont-1,d)
        
main()
