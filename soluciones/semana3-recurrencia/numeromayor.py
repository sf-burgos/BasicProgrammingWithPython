from sys import stdin
x=int(stdin.readline().strip())
def zum (x):
    if x<=9:
        return x
    else:
        y=x%10
        z= zum(x//10)
        if y>z:
            return y
        else:
            return z
def zuma (x):
    if x<=9:
        return x
    else:
        y=x%10
        z= zuma(x//10)
        if y>z:
            return z
        else:
            return y        
print (zum(x)+zuma(x))

     
