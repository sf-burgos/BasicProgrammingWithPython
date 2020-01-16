from sys import stdin
n=int(stdin.readline())
x=[int(xx) for xx in stdin.readline().strip().split(" ")]
y=[int(yy) for yy in stdin.readline().strip().split(" ")]
z=x+y
def xxx(n,x,y):
    cont=0
    for niveles in range (1,n+1):
        if niveles in z:
            cont+=1
        else:
            cont+=0
    
    return cont
def main():
    xxx(n,x,y)
    if n==xxx(n,x,y):
        print ("I become the guy.")
    else:
        print ("Oh, my keyboard!")
main()
