from sys import stdin
ent=str(stdin.readline().strip())
print(ent)
lista=[]
if "Z" in ent:
    print(0)
    #break
else:
    for j in range(len(ent)):
        if ent[j]=="R":
            for i in range(len(ent)):
                if ent[i]=="D":
                    x=abs(j-i)
                    lista.append(x)

print(min(lista))
