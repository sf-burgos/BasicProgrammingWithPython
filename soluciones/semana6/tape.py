from sys import stdin
def main():
    entrada=str(stdin.readline().strip())
    entrada=str(stdin.readline().strip())
    cadena=""
    while entrada!="___________":
        cont=8
        cont2=0
        entrada=entrada[1:-1]
##for de izquierda a derecha


        
        if entrada==" o . ":
            print(' ',end="")
        else:
            for i in range(len(entrada)):
                cont-=1
                if entrada[i]==".":
                    break
                elif entrada[i]=="o":
                    cont2+=2**cont

            cont=-1
##derecha a izquierda





            
            if len(entrada)>2:
                for j in range(-1,len(entrada)*-1,-1):
                    cont+=1
                    if entrada[j]==".":
                        break
                    elif entrada[j]=="o":
                        cont2+=2**cont
                
                print(chr(cont2),end="")


                
            entrada=str(stdin.readline().strip())
        

main()

