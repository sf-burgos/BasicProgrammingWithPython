from sys import stdin

def log (x,con):
    if x>0:
        a=x%10
        if a%2==0:
            con=con*(a)
            log(x//10,con)  
        else:
            log(x//10,con)
    else:
         print ("La multiplicacion de los digitos pares es",con)

def main():
    x=int(stdin.readline().strip())
    con=1
    log(x,con)     
main()      
