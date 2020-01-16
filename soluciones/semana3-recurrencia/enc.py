from sys import stdin
p=(stdin.readline().strip())

p=p.lower()
def letra(frase,x,y,pal):
    if p==0 and len(p)-1:
        if frase[x]==frase[y]:
            letra(frase,x+1,y-1,pal-1)
        else:
            print("Go home Diana")

    else:
        print("Muua!")

letra(p,0,len(p)-1,len(p))
