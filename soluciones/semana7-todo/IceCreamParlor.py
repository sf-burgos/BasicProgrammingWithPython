from sys import stdin
def helado():
    t=int(stdin.readline().strip())
    for i in range(t):
        m=int(stdin.readline().strip())
        n=int(stdin.readline().strip())
        lista= [int(x) for x in stdin.readline().strip().split(' ')]
        bus="0"
        pos=""
        cont=1
        for i in lista:
            if i==1:
                pass
            else m//i==0:
                
                bus=bus+str("+")+str(i)
                x=eval(bus)
                pos=pos+str(cont)+" "
                if x==m:
                    break
                cont+=1
        print(pos)
        
        
            
     
helado()
