from sys import stdin
l=int(stdin.readline().strip())
b=int(stdin.readline().strip())
s=int(stdin.readline().strip())

print(((l+s-1)//s)*((b+s-1)//s))
