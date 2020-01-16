from sys import stdin
def main():
    n=int(stdin.readline().strip())
    suma=n
    while n>=3:
        suma+=(n/3)
        n=n//3+n%3
        suma=int(suma)
    if suma%3>=2:
        print(int(suma)+1)
    else:
        print(int(suma))
    
main()
