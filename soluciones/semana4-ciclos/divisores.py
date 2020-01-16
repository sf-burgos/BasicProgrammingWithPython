from sys import stdin
n = int(stdin.readline())
def div (a):
    for i in range (1, n): 
        if (n%i==0): 
            print (i)
    print (n)
            
            
            
div(n)

