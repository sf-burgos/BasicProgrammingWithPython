from sys import stdin
def main():
    
    i=[int(xx) for xx in stdin.readline().strip().split(",") ]
    j=[int(xx) for xx in stdin.readline().strip().split(",") ]
    if (2<=len(i)<=1000 and 2<=len(j)<=1000):
        lista=[]
        for alfa in  range(len(i)):
            if i[alfa]==j[alfa]:
                lista.append(0)
            elif i[alfa]>j[alfa]:
                lista.append((i[alfa]//2))
                i[alfa]-=(i[alfa]//2)
            else:
                lista.append((j[alfa]//2))
                j[alfa]-=(j[alfa]//2)
        primero=""
        segundo=""
        tercero=""
        for k in range(len(i)):
            if k!=len(i)-1: 
                primero+=str(lista[k])+","
                segundo+=str(i[k])+","
                tercero+=str(j[k])+","
            else:
                primero+=str(lista[k])
                segundo+=str(i[k])
                tercero+=str(j[k])
                
            
        print("Laura",primero)    
        print("Lupe",segundo)
        print("Carlos",tercero)
    else:
        return
        
main()
