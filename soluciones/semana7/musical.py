from sys import stdin
def main():
    longitud=int(stdin.readline().strip())
    while longitud!=0:
        cont=0
        rangos=[int(x) for x in stdin.readline().strip().split()]

        for i in range(1,len(rangos)-1):
            if rangos[i-1]>rangos[i]<rangos[i+1] or rangos[i-1]<rangos[i]>rangos[i+1]:
                cont+=1
        

        if (rangos[-1]>rangos[0]<rangos[1]):
            cont+=1
        if  (rangos[-2]<rangos[-1]>rangos[0]):
            cont+=1
        if (rangos[-1]<rangos[0]>rangos[1]):
            cont+=1

        if (rangos[-2]>rangos[-1]<rangos[0]):
            cont+=1
        print(cont)











        


















        longitud=int(stdin.readline().strip())


main()    
