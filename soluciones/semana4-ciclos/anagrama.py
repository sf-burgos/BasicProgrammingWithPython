from sys import stdin
#n= [str(arr_temp) for arr_temp in stdin.readline().strip().split(" ")]

#Amor Roma
def anagrama(n):
    z=n[0].lower()
    y=n[1].lower()
    p=[]
    o=[]
    for palabra1 in z:
        p.append(palabra1)
        p.sort()
    for palabra2 in y:
        o.append(palabra2)
        o.sort()
    if o==p:
        return ("Anagrama")
    else:
        return ("No")
       

def main():
    n= stdin.readline().strip()
    while n!="":
        n=[str(arr_temp) for arr_temp in n.split(" ")]
        anagrama(n)
        print (anagrama(n))
        n= stdin.readline().strip()
    
main()
#<<=[str(i)for i in n]
