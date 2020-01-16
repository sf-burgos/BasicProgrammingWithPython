from sys import stdin
def main():
    n=[int(xx) for xx in stdin.readline().strip().split(" ")]
    if (mult(n)==True or resta(n)==True or s(n)==True):
        print("Possible")
    else:
        print("Impossible")
def mult(lista):
    v=""
    for i in range(0,len(lista)):
        v+=str(lista[i])
        if eval(v)==23:
            return (True)
        else:
            v+=str("*")
def resta(lista):
    v=""
    for i in range(0,len(lista)):
        v+=str(lista[i])
        if eval(v)==23:
            return (True)
        else:
            v+=str("-")
def s(lista):
    v=""
    for i in range(0,len(lista)):
        v+=str(lista[i])
        if eval(v)==23:
            return (True)
        else:
            v+=str("+") 
main()
