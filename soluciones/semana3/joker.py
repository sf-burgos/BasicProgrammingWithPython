from sys import stdin
def main():
    n=int(stdin.readline().strip())
    dic={}
    bajas=["2","3","4","As"]
    medias=["5","6","7"]
    altas=["8","9","10","K","J","As","Q"]
    b=0
    med=0
    alt=0
    bajas_barajas=16*n
    medias_barajas=12*n
    altas_barajas=28*n
    total_cartas=(52*n)-5
    lista=[]
    for i in range(5):
        m=str(stdin.readline().strip())
        lista.append(m)
        if m not in dic:
            dic[m]=1
        else:
            dic[m]+=1     
        if m in bajas:
            b+=1
        if m in altas:
            alt+=1
        if m in medias:
            med+=1
    
    for i in lista:
        if (i in bajas) or (i in altas) or (i in medias):
            pass
        else:
            print("ERROR EN LOS DATOS")
            return
    for x in dic:
        if dic[x]<=4*n:
            p=True
        else:
            p=False
            print("ERROR EN LOS DATOS")
            return
    if n<0 or n>4:
        print("ERROR EN LOS DATOS")
        return
    if p:
        print("La probabilidad de cartas bajas es:",str(round(((bajas_barajas-b)/total_cartas)*100,2))+'%')
        print("La probabilidad de cartas medias es:",str(round(((medias_barajas-med)/total_cartas)*100,2))+'%')
        print("La probabilidad de cartas altas es:",str(round(((altas_barajas-alt)/total_cartas)*100,2))+'%')
main()
