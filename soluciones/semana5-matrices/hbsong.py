from sys import stdin

##n=["Happy", "birthday", "to", "you", "Happy", "birthday", "to", "you", "Happy", "birthday", "to","Rujia", "Happy", "birthday", "to" ,"you"]

def salida():
    n=int(stdin.readline().strip())
    p=[]
    while n>0:
        n=n
        persona=stdin.readline().strip()
        p.append(persona)
    cancion=["Happy", "birthday", "to", "you", "Happy", "birthday", "to", "you", "Happy", "birthday", "to","Rujia", "Happy", "birthday", "to" ,"you"]
        n-=1
    print(p)
        

        
salida()
        
    

    



