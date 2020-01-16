from sys import stdin
import sys
def main():
##    SUN=1
##    MON=2
##    TUE=3
##    WED=4
##    THU=5
##    FRI=6
##    SAT=7
    lista1=["JAN","MAR","MAY","JUL","AUG","OCT","DEC"]
    lista2=["APR","JUN","SEP","NOV"]
    lista3=["FEB"]
    MON=[1,2,3,4,5,6,7]
    TUE=[2,3,4,5,6,7,1]
    WED=[3,4,5,6,7,1,2]
    THU=[4,5,6,7,1,2,3]
    FRI=[5,6,7,1,2,3,4]
    SAT=[6,7,1,2,3,4,5]
    SUN=[7,1,2,3,4,5,6]
    
    n=[str(arr_temp) for arr_temp in stdin.readline().strip().split(" ")]
    while n!=[""]:
        z=n[0]
        y=n[1]
        listavacia=[]
        p=False
        #monday
        if y=="MON":
            for i in range(4):
                for i in MON:
                    listavacia.append(i)
            if z in lista1:
                listavacia.append(1)
                listavacia.append(2)
                listavacia.append(3)
            elif z in lista2:
                listavacia.append(1)
                listavacia.append(2)
            elif z in lista3:
                listavacia.append(1)
            else:
                print("ERROR IN MONTH!")
                p=True
                pass
        #TUESDAY
        elif y=="TUE":
            for i in range(4):
                for i in TUE:
                    listavacia.append(i)
            if z in lista1:
                listavacia.append(2)
                listavacia.append(3)
                listavacia.append(4)
            elif z in lista2:
                listavacia.append(2)
                listavacia.append(3)
            elif z in lista3:
                listavacia.append(2)
            else:
                print("ERROR IN MONTH!")
                p=True
                pass
        #WEDNESDAY
        elif y=="WED":
            for i in range(4):
                for i in WED :
                    listavacia.append(i)
            if z in lista1:
                listavacia.append(3)
                listavacia.append(4)
                listavacia.append(5)
            elif z in lista2:
                listavacia.append(3)
                listavacia.append(4)
            elif z in lista3:
                listavacia.append(3)
            else:
                print("ERROR IN MONTH!")
                p=True
                pass
        #THUSTDAY
        elif y=="THU":
            for i in range(4):
                for i in THU:
                    listavacia.append(i)
            if z in lista1:
                listavacia.append(4)
                listavacia.append(5)
                listavacia.append(6)
            elif z in lista2:
                listavacia.append(4)
                listavacia.append(5)
            elif z in lista3:
                listavacia.append(4)
            else:
                print("ERROR IN MONTH!")
                p=True
                pass
        #FRIDAY
        elif y=="FRI":
            for i in range(4):
                for i in FRI:
                    listavacia.append(i)
            if z in lista1:
                listavacia.append(5)
                listavacia.append(6)
                listavacia.append(7)
            elif z in lista2:
                listavacia.append(5)
                listavacia.append(6)
            elif z in lista3:
                listavacia.append(5)
            else:
                print("ERROR IN MONTH!")
                p=True
                pass
        #SATURDAY
        elif y=="SAT":
            for i in range(4):
                for i in SAT:
                    listavacia.append(i)
            if z in lista1:
                listavacia.append(6)
                listavacia.append(7)
                listavacia.append(1)
            elif z in lista2:
                listavacia.append(6)
                listavacia.append(7)
            elif z in lista3:
                listavacia.append(6)
            else:
                print("ERROR IN MONTH!")
                p=True
                pass
        #SUNDAY
        elif y=="SUN":
            for i in range(4):
                for i in MON:
                    listavacia.append(i)
            if z in lista1:
                listavacia.append(7)
                listavacia.append(1)
                listavacia.append(2)
            elif z in lista2:
                listavacia.append(7)
                listavacia.append(1)
            elif z in lista3:
                listavacia.append(7)
            else:
                print("ERROR IN MONTH!")
                p=True
                pass
        else:
            p=True
            print("ERROR IN DAY!")
        if p==False:
            codigo=listavacia.count(5)+listavacia.count(6)
            print(codigo)
         
        n=[str(arr_temp) for arr_temp in stdin.readline().strip().split(" ")]
    
       
       
                
    
main()

