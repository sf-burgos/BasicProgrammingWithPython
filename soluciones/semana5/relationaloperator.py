from sys import stdin
def main():
    n=int(stdin.readline().strip())
    for numero in range(n):
        x,y=list(map(int,stdin.readline().split()))
        print(operaciones(x,y))
def operaciones(x,y):            
    if x<y:
        return("<")
    elif x>y:
        return(">")
    else:
        return("=")
main()
