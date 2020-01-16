from sys import stdin
n=int(stdin.readline().strip())
def matrizdeloscapos(n):
    x=[]
    for i in range(n):
        x.append(1)
    print(str(x).replace(" ",""))
    d=0
    z=3
    while n>1:
        for i in range (0,len(x)):
            x[i]+=z
                
        z+=2
        n-=1
        
        print(str(x).replace(" ",""))

matrizdeloscapos(n)
