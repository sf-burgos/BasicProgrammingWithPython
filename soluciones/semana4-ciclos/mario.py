from sys import stdin
#1 4 2 2 3 5 3 4

n=[int(xx) for xx in stdin.readline().strip().split(" ")]
def paredes (n):
    if len[n]>10:
        return paredes
    else:
        altos=0
        bajos=0
        pos1=-1
        pos2=0
        for mario in n:
            pos1+=1
            pos2+=1
            if n[pos1]>n[pos2]:
                bajos+=1
            else:
                n[pos1]<n[pos2]
                altos+=1
        print (altos)
        print (bajos)
        

paredes (n)
