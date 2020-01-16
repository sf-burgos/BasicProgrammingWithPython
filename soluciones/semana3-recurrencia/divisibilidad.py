from sys import stdin

def zum (x,y,t):
    if x>0:
        a=x%10
        if a%y==0:
            t=t+str(a)
            zum(x//10,y,t)  
        else:
            zum(x//10,y,t)
    else:
         print (t)

def main():
    x=int(stdin.readline().strip())
    y=int(stdin.readline().strip())
    t=""    
    zum(x,y,t)     
main()      
