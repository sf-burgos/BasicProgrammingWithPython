from sys import stdin
def main():
    m=[int(i) for i in stdin.readline().strip().split(" ")]
    p=[str(i) for i in stdin.readline().strip()]
    i=0
    z=m[1]
    while z>0:
        while i<len(p)-1:
                if p[i]=="B" and p[i+1]=="G":
                    p[i]="G"
                    p[i+1]="B"
                    i+=2

                else:
                    i+=1
        z-=1
        i=0
    c=""
    for ii in p:
        c+=ii
    print(c)
    
    

        
main()
            
        
