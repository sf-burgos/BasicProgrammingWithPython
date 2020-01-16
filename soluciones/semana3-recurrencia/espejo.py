from sys import stdin
x= str(stdin.readline().strip())
def invertir (palabra,cos):
    if cos>=0:
        return palabra[cos]+invertir(palabra,cos-1)
    else:
         return ""

def cup (palabra):
    return invertir(palabra,len(palabra)-1)

print (cup(x))
