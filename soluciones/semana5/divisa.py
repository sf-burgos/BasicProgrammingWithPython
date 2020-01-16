from sys import stdin
def main():
    k=int(stdin.readline().strip())
    while k!=0:
        limites=[int(xx)for xx in stdin.readline().strip().split(" ")]
        x=limites[0]
        y=limites[1]
        for i in range(k):
            coordenadas=[int(xx)for xx in stdin.readline().strip().split(" ")]
            a=coordenadas[0]
            b=coordenadas[1]
            if (a==x or b==y):
                print("divisa")
            elif (a>x and b>y):
                print("NE")
            elif (a<x and b>y):
                print("NO")
            elif (a<x and b<y):
                print("SO")
            else:
                print("SE")
        k=int(stdin.readline().strip())
main()
