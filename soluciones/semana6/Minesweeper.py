from sys import stdin
def entrada(listamayor):
    lista=[]
    lineas=str(stdin.readline().strip())
    lista.append(".")
    for i in range(len(lineas)):
        lista.append(lineas[i])
    lista.append(".")
    listamayor.append(lista)
def instrucciones(listamayor,numeros,numeros2):
    for i in range(numeros+2):
        for j in range(numeros2+2):
            if listamayor[i][j]=='.':
                listamayor[i][j]=0
    for i in range(numeros+1):
        for j in range(numeros2+1):
            if listamayor[i-1][j-1]=="*":
                if listamayor[i][j]=="*":
                    pass
                else:
                    listamayor[i][j]=listamayor[i][j]+1
            if listamayor[i-1][j]=="*":
                if listamayor[i][j]=="*":
                    pass
                else:
                    listamayor[i][j]=listamayor[i][j]+1
            if listamayor[i-1][j+1]=="*":
                if listamayor[i][j]=="*":
                    pass
                else:
                    listamayor[i][j]=listamayor[i][j]+1
            if listamayor[i][j-1]=="*":
                if listamayor[i][j]=="*":
                    pass
                else:
                    listamayor[i][j]=listamayor[i][j]+1
            if listamayor[i][j+1]=="*":
                if listamayor[i][j]=="*":
                    pass

                else:
                    listamayor[i][j]=listamayor[i][j]+1
            if listamayor[i+1][j-1]=="*":
                if listamayor[i][j]=="*":
                    pass
                else:
                    listamayor[i][j]=listamayor[i][j]+1
            if listamayor[i+1][j]=="*":
                if listamayor[i][j]=="*":
                    pass
                else:
                    listamayor[i][j]=listamayor[i][j]+1
            if listamayor[i+1][j+1]=="*":
                if listamayor[i][j]=="*":
                    pass

                else:
                    listamayor[i][j]=listamayor[i][j]+1
    #del listamayor[0]
    #del listamayor[len(listamayor)]
    new=listamayor[1::]
    del new[-1]
    r=len(new)
    z=0
    while z<r:
        result=""
        final=new[z]
        del final[0]
        del final[-1]
        for i in final:
            result+=str(i)
        print(result)
    
        z+=1
        
    
def main():
    field=1
    numeros=[int(xx)for xx in stdin.readline().strip().split(" ")]
    while numeros[0]!=0 or numeros[1]!=0:
        listamayor=[]
        punto="."
        listapunto=[]
        punto=punto*(numeros[1]+2)
        for i in punto:
            listapunto.append(i)
        listamayor.append(listapunto)
        for i in range (numeros[0]):
            entrada(listamayor)
        listamayor.append(listapunto)
        print("Field #"+str(field)+":")
        instrucciones(listamayor,numeros[0],numeros[1])
        field+=1
        numeros=[int(xx)for xx in stdin.readline().strip().split(" ")]
        if numeros[0]!=0 or numeros[1]!=0:
            print("")
        
main()
