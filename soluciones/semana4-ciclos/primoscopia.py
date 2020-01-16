from sys import stdin

def primo(n, cont):
        if n==1 or n==2:
            cont+=1
        elif n>2:
             if n%2==0:
                 cont+=0
             else:
                for x in range(1,n+1):
                    if x ==n:
                        cont+=1
                    elif n%x==0 and x!=1 :
                        cont+=0
                        break
        print (cont) 
                
def main():
        s=int(stdin.readline())
        for i in range(s):
            n=int(stdin.readline())
        primo(s,cont=0)
        
main()
