from sys import stdin
#OOXXOXXOOO
#cuenta=0
def contador(lista):
    cuentaO=0
    cuentaX=0
    num=0
    for caracter in lista:
        if caracter=="O":
            if num==0:
                cuentaO+=1
                num+=1
            else:
                num+=1
                cuentaO+=(num)
        elif caracter=="X":
            cuentaX+=0
            num=0
            
    print(cuentaO)    
def main():
    s=int(stdin.readline())
    for i in range(s):
        lista=(stdin.readline())
        contador(lista)

        
main()
