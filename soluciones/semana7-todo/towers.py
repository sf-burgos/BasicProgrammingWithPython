from sys import stdin
n=int(stdin.readline().strip())
e=[int(i)for i in stdin.readline().strip().split(" ")]
def p():
    c=0
    d=[]
    for aa in e :
       
        if aa in d:
            pass
        else:
            d.append(aa)

    for i in d:
        if e.count(i)>c:
            c=e.count(i)
    print(c,len(d))
p()
