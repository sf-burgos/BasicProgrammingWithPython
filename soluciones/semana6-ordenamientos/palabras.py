from sys import stdin
def palabra(n):
    singular=""
    plural=""
    if len (n)==2:
        singular=singular+str(n[0])
        plural=plural+str(n[1])
        print(singular)
        print(plural)
    else:
        pp=busqueda(singular,n)
        if pp!=-10:
            print(plural[pp])
        
            """else:
            if f[-1]=="y":
                vocal=["a","e","i","o","u"]
                if f[-2] in vocal:
                    f=f+str("s")
                else:
                    f=f.replace("y","ies")
            elif f[-1]=="o":
                f=f+str("ies")
            elif f[-1]=="s": 
                f=f+str("ies")
            elif f[-2]=="c" and f[-1]=="h":
                f=f+str("es")
            elif f[-1]=="x":
                f=f+str("es")
            else :
                f=f+str("s")"""

  

def busqueda(singular,x):
    i=0
    flag=-10
    for z in singular:
        if z ==x:
            flag=i
            return flag
        i=i+1
    return flag
def main():
    for i in range (0,3):
        n=str(stdin.readline().strip().split(" "))
        palabra(n)
main()

