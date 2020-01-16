from sys import stdin
def recu(a):
    if a==0 :
        return 0
    else:
        return a%10+recu(a//10)
def main():
    a=int(stdin.readline().strip())
    b=int(stdin.readline().strip())
    x= recu(a)
    y= recu(b)
    if x==y:
        print (a,"y",b,"si son familia")

    else: 
        print (a,"y",b,"no son familia")
main()





 


