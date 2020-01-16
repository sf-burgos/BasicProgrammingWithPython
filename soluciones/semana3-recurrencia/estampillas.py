from sys import stdin
n= int(stdin.readline().strip())

def est(x):
    if x==1:
        return 3
    else:
        return (est(x-1)*2)+10+est(x-1)
print(est(n),"estampillas")

