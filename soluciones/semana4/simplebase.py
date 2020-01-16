from sys import stdin
import sys
def decimal(numero):
    if numero<16:
        return str(numero)
    else:
        numero2=numero%16
        return  str(numero2),decimal(numero//16)
def hexadecimal(x,lista,operacion):
    if x>=(len(lista)):
        return operacion
    else:
        if lista[x]=="A":
            operacion+=10*(16**int(x))
            return hexadecimal(x+1,lista,operacion)
        elif lista[x]=="B":
            operacion+=11*(16**int(x))
            return hexadecimal(x+1,lista,operacion)
        elif lista[x]=="C":
            operacion+=12*(16**int(x))
            return hexadecimal(x+1,lista,operacion)
        elif lista[x]=="D":
            operacion+=13*(16**int(x))
            return hexadecimal(x+1,lista,operacion)
        elif lista[x]=="E":
            operacion+=14*(16**int(x))
            return hexadecimal(x+1,lista,operacion)
        elif lista[x]=="F":
            operacion+=15*(16**int(x))
            return hexadecimal(x+1,lista,operacion)
        else:
            operacion+=(int(lista[(x)]))*(16**int(x))
            return hexadecimal(x+1,lista,operacion)
def main():
    entrada=str(stdin.readline().strip())

    #while entrada!="":
    if len(entrada)<=1:
        print("0x"+str(entrada))
    elif entrada[1]=="x":
        lista=entrada[2::]
        lista=lista[::-1]
        x=0
        operacion=0
        print((hexadecimal(x,lista,operacion)))
    else:
        if int(entrada)<=0:
            return
        a=str((decimal(int(entrada))))
        b="0x"
        a=a.replace("(","")
        a=a.replace(")","")
        a=a.replace(",","")
        a=a.replace("'","")
        a=a.split(" ")
        a=a[::-1]
        for i in a:
            if i=="10":
                b+="A"
            elif i=="11":
                b+="B"
            elif i=="12":
                b+="C"
            elif i=="13":
                b+="D"
            elif i=="14":
                b+="E"
            elif i=="15":
                b+="F"
            else:
                b+=i
        print(b)
        #entrada=str(stdin.readline().strip())
            
        
main()
