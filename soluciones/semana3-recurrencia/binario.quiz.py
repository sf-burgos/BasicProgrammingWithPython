from sys import stdin

def binario(num):
    x=num%2
    if num==1:
        return str(1)
    elif num==0:
        return str(0)
    else:
        return str(binario(num//2))+str(x)
def main():
    num=int(stdin.readline().strip())
    bi=binario(num)
    print(bi)
main()
