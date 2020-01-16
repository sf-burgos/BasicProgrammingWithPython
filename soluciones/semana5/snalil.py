from sys import stdin
def main():
    n=[int(x) for x in stdin.readline().strip().split()]
    while n!=[0,0,0,0]:
        altura=n[0]
        alt=0
        dia=n[1]
        noche=n[2]
        pat=n[3]
        cont=0
        a=(dia*pat)/100
        
        while altura>alt:
            cont+=1
            
            if alt>=0:
                alt=alt+(dia)
                if altura>=alt:
                    alt-=noche
                dia=dia-(a)
                
            if alt<0:
                break

        if alt<0:
            print("failure on day",cont)
        else:
            print("success on day",cont)
        n=[int(x) for x in stdin.readline().strip().split()]

main()

