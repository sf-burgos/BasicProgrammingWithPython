from sys import stdin
def main():
    
    n=int(stdin.readline().strip())
    cont=1
    for i in range(n):
        entrada=[int(xx) for xx in stdin.readline().strip().split(" ")]
        entrada.sort()
        a=entrada[0]
        b=entrada[1]
        c=entrada[2]
        print("Case "+str(cont)+": "+str(tipo(a,b,c)))
        cont+=1
def tipo(a,b,c):
    if c<(a+b):
        pass
    else:
        return"Invalid"
    if (a or b or c)<=0:
        return"Invalid"
    if (a==b) and(a==c) and(b==c):
        return "Equilateral"
    elif a==b or a==c or b==c:
        return "Isosceles"
    else:
        return "Scalene"
        
main()
