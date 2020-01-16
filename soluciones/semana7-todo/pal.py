from sys import stdin
import operator
def main():
    d=""
    lista=[]
    let="QWERTYUIOPASDFGHJKLÑZXCVBNM"
    n=int(stdin.readline().strip())
    while n!=0:
        a=str(stdin.readline().strip())
        a=a.upper()
        a=a.replace(" ","")
        a=a.replace(".","")
        d=d+str(a)
        n-=1
    for i in d:
        if i in let:
            lista.append(i)
        else:
            d=d.replace(i,"")
    lista.sort()
    dic={}
    mem={}
    keys=list(dic.keys())
    for i in lista: 
        dic[i]=lista.count(i)
        if dic[i] not in mem:
            mem[dic[i]]=[i]
        else:
            if i not in mem[dic[i]]:
                mem[dic[i]].append(i)
                mem[dic[i]].sort()
    q=sorted(mem)
    q.reverse()
    for x in q:
        for y in mem[x]:
            print(y,x)
##    resultado=sorted(dic.items(), key=operator.itemgetter(1)) 
##    resultado.reverse()
    c=0
##    print(resultado)
##    for i in resultado:
##        print(i[0],i[1])
##    print(dic)

    
main()
