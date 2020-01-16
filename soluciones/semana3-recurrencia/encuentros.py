from sys import stdin

def pal (p,b):
    if b>=0:
        return p[b]+pal(p,b-1)
    else:
        return ""
def inv ():
    return pal (n,len(n)-1)
n=stdin.read().strip()
n=n.lower()
x=inv()
if x==n and len (n)%2==0:
    print ("Muua!")
else:
    print ("Go home Diana")
