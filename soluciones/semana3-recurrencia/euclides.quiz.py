from sys import stdin
def div(x,y):    
    if x%y==0:        
        return y    
    elif y%x==0:        
        return x 
    else:       
        if x>y:           
            return div(x%y,y)
        else:           
            return div(x,y%x) 
def main():    
    x=int(stdin.readline())  
    y=int(stdin.readline())  
    print(div(x,y))

main()
