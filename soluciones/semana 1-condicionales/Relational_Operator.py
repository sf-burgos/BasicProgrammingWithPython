from sys import stdin
m= int(stdin.readline().strip())
n= int(stdin.readline().strip())
if m>n:
    print (">")
if m<n:
    print ("<")
if m==n:
    print ("=")
