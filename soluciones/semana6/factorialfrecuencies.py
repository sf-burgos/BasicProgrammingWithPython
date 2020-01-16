from sys import stdin
from math import *
def main():
    
    entrada=int(stdin.readline().strip())
    while entrada!=0:
        fac=str(factorial(entrada))
        cont0=fac.count("0")
        cont1=fac.count("1")
        cont2=fac.count("2")
        cont3=fac.count("3")
        cont4=fac.count("4")
        cont5=fac.count("5")
        cont6=fac.count("6")
        cont7=fac.count("7")
        cont8=fac.count("8")
        cont9=fac.count("9")
        print(str(entrada)+str("! --"))
        print("(0)".rjust(6," ")+str(cont0).rjust(5," "),"(1)".rjust(6," ")+str(cont1).rjust(5," "),"(2)".rjust(6," ")+str(cont2).rjust(5," "),"(3)".rjust(6," ")+str(cont3).rjust(5," "),"(4)".rjust(6," ")+str(cont4).rjust(5," "))
        print("(5)".rjust(6," ")+str(cont5).rjust(5," "),"(6)".rjust(6," ")+str(cont6).rjust(5," "),"(7)".rjust(6," ")+str(cont7).rjust(5," "),"(8)".rjust(6," ")+str(cont8).rjust(5," "),"(9)".rjust(6," ")+str(cont9).rjust(5," "))

              #+str("(1)").rjust(6," ")+str(cont1).rjust(5," "))+str("(2)").rjust(6," ")+str(cont2).rjust(5," ")+str("(3)").rjust(6," ")+str(cont3).rjust(5," ")+str("(4)").rjust(6," ")+str(cont4).rjust(5," ")

        

        entrada=int(stdin.readline().strip())


main()

    
    
