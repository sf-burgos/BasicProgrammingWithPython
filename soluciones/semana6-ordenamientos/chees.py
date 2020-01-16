from sys import stdin
def ajedrez(lista):
    if lista[0]==lista[2] and lista[1]==lista[3]:
        return 0
    elif lista[0]+lista[1]==lista[2]+lista[3]:
        return 1
    else:
        return 2
     
def main():
    lista=[int(arr_temp) for arr_temp in stdin.readline().strip().split(" ")]
    while lista[0]!=0:
        print(ajedrez(lista))
        lista=[int(arr_temp) for arr_temp in stdin.readline().strip().split(" ")]
    
main()
