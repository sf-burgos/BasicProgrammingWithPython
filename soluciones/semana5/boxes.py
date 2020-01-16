from sys import stdin
#n=int(stdin.readline())
#s=[int(arr_temp) for arr_temp in stdin.readline().strip().split(" ")]

def entrada(n,s):
    h=0
    suma=0
    for i in s:
        suma +=i
        numerodecuadros=suma//n
    for j in s:
        m=j-numerodecuadros
        if m>0:
            h=h+m
    return(h)

def main():
    n=int(stdin.readline())
    cont=1
    while n!=0:
        s=[int(arr_temp) for arr_temp in stdin.readline().strip().split(" ")]
        print("Set #"+str(cont))
        print ("The minimum number of moves is",str(entrada(n,s))+".")
        cont+=1
        n=int(stdin.readline())
        print("")
        
        
    







main()
