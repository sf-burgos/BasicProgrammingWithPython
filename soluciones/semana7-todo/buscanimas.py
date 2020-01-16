from sys import stdin
o=0
x=[int(i) for i in stdin.readline().split(" ")]
while x[0]!=0 and x[1]!=0:
    mat=[]
    for i in range(x[0]):
        b=stdin.readline().strip()
        c=["."]
        for k in range(len(b)):
            c.append(b[k])
        c.append(".")    
        mat.append(c)
    g=[".","."]
    for i in range(x[1]):
        g.append(".")    
    mat.insert(0,g)
    mat.insert(len(mat),g)
    print(mat)
        
    def minas(l,x):
         t= [[0 for j in range(x[1])]for i in range(x[0])]
         for i in range(1,len(l)-1):
           for j in range(1,len(l[0])-1):
             if l[i-1][j-1]=="*":
                 t[i-1][j-1]+=1
             if l[i-1][j]=="*":
                 t[i-1][j-1]+=1
             if l[i-1][j+1]=="*":
                 t[i-1][j-1]+=1
             if l[i][j-1]=="*":
                 t[i-1][j-1]+=1
             if l[i][j+1]=="*":
                 t[i-1][j-1]+=1
             if l[i+1][j-1]=="*":
                 t[i-1][j-1]+=1
             if l[i+1][j]=="*":
                 t[i-1][j-1]+=1
             if l[i+1][j+1]=="*":
                 t[i-1][j-1]+=1
             if l[i][j]=="*":
                 t[i-1][j-1]="*"    
         return t        
    h=(minas(mat,x))
    o+=1
    print(("Field #{}:").format(o)
)
    for i in range(len(h)):
        s=""
        for j in range(len(h[0])):
          s+=str(h[i][j])
        print(s)
    print("")    
    x=[int(i) for i in stdin.readline().split(" ")]
