from sys import stdin
def main():
    matriz=[]
    n=5
    while n>0:
        k=[int(x) for x in stdin.readline().strip().split()]
        matriz.append(k)
        n-=1
    if matriz[0][0]==1 or matriz[0][4]==1 or matriz[4][0]==1 or matriz[4][4]==1:
        print(4)
    elif matriz[3][0]==1 or matriz[3][4]==1 or matriz[1][4]==1 or matriz[1][0]==1 or matriz[0][1]==1 or matriz[0][3]==1 or matriz[4][1]==1 or matriz[4][3]==1:
        print (3)
    elif matriz[0][2]==1 or matriz[2][0]==1 or matriz[2][4]==1 or matriz[1][1]==1 or matriz[3][1]==1 or matriz[4][2]==1 or matriz[2][4]==1 or matriz[3][1]==1:
        print(2)
    elif matriz[1][2]==1 or matriz[2][1]==1 or matriz[2][3]==1 or matriz[3][2]==1:
        print(1)
    else:
        print(0)
main()

