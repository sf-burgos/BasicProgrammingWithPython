from sys import stdin
def main():
    entrada=[str(xx) for xx in stdin.readline().strip().split(" ")]
    x=entrada[0]
    operador=entrada[1]
    y=entrada[2]
    x=int(str(x),16)
    y=int(str(y),16)  
    if operador=="+":
        salida=int(x)+int(y)
    else:
        salida=int(x)-int(y)
    x=binario(int(x))
    y=binario(int(y))
    x=x.zfill(13)
    y=y.zfill(13)
    print(x,operador,y,"=",salida)
def binario(num):
    entrada=num%2
    if num==1:
        return str(1)
    elif num==0:
        return str(0)
    else:
        return str(binario(num//2))+str(entrada)

main()
    
