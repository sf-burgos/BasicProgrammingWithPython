from sys import stdin
def banana ():
    k=int(stdin.readline().strip())
    n=int(stdin.readline().strip())
    w=int(stdin.readline().strip())
    x=int(k*(w*(w+1))/2)
    if x<=n:
        print("0")
    else:
        print (x-n)
banana()

    
   
