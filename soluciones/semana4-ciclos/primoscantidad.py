from sys import stdin

def primo(n):
        if n==1 or n==2:
            print("Primo")
        elif n>2:
             if n%2==0:
                 print("No Primo")
             else:
                for x in range(1,n+1):
                    if x ==n:
                        print("Primo")
                    elif n%x==0 and x!=1 :
                        print("No Primo")
                        break
def cantidad  (s):
    for i in n:
        i=int(i)
        lista_2.append(i)
                
def main():
    n=int(stdin.readline())
    cantidad(n)
        
main()
