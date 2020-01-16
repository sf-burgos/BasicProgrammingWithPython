from sys import stdin
n= float(stdin.readline().strip())        
m= float(stdin.readline().strip())
ñ= float(stdin.readline().strip())
if n+ñ<m or n+m<ñ or m+ñ<n:
    print ("incorrecto")
elif n==m and m==ñ and ñ==n:
    print ("equilatero")

elif n==m!=ñ or n==ñ!=m or m==ñ!=n: 
    print ("isosceles")

elif n!=m and n!=ñ and m!=ñ:
    print ("escaleno ")

