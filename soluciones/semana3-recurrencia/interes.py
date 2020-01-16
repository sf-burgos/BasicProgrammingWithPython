from sys import stdin
a=int (stdin.readline().strip())
interes=float(stdin.readline().strip())
n=float(stdin.readline().strip())
def pf(a,interes,n):
    if n==0:
         return a
    else:
        return ((1+interes)*pf(a,interes,n-1))

print ("$"+str(round(pf(a,interes,n),1)))
