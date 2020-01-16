from sys import stdin
def main():
    n=int(stdin.readline().strip())
    while n!=0:
        ent=str(stdin.readline().strip())
        lista=[]
        if "Z" in ent:
            lista.append(int(0))
        else:
            for j in range(len(ent)):
                if ent[j]=="R":
                    for i in range(len(ent)):
                        if ent[i]=="D":
                            x=abs(j-i)
                            lista.append(x)

        print(min(lista))
        n=int(stdin.readline().strip())

main()
