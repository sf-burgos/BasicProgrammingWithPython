from sys import stdin
n=int(stdin.readline().strip())
m=int(stdin.readline().strip())
p=n+m
if n<0:
    n=str("(")+str(n)+str(")")
if m<0:
    m=str("(")+str(m)+str(")")
print((str(n)+str("+")+str(m)+str("=")+str(p)))
