from sys import stdin
def fac():
    lista=[]
    dic={1:1,2:2}
    n=1
    for n in range(1,10001):
        if n==0:
            print(str(0).rjust(5," "),"->","1")
        elif n not in dic:
            cont=dic[len(dic)]
            for i in range (len(dic)+1,n+1):
                cont*=i
                dic[i]=cont

            q=str(dic[n])
            for x in range(-1,-1*len(q)-1,-1):
                if q[x] != "0":
                        
                    lista.append(q[x])
                    break

        else:
            q=str(dic[n])
            for x in range(-1,-1*len(q)-1,-1):
                if q[x] != "0":
                    lista.append(q[x])
                    break
    
    print(lista)
        
fac()


        
    
        


