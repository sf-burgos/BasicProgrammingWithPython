from sys import stdin
def hacker(n):
    lista=["h","a","c","k","e","r","r","a","n","k"]
    lista2=[]
    o=0
    for i in n:
        if i==lista[o]:
            lista2.append(i)
            o+=1       
        if lista==lista2:
         return("YES")
    
    return("NO")
def main():
    m=int(stdin.readline().strip())
    n=str(stdin.readline().strip())
    while m!=0:
        print(hacker(n))
        n=str(stdin.readline().strip())
        m=m-1
main()
