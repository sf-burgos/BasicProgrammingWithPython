from sys import stdin
n= int(stdin.readline().strip())        
m= int(stdin.readline().strip())

n1= n%10
n2= (n//10)%10
n3= (n//100)%10
n4= n//1000

m1= m%10
m2= (m//10)%10
m3= (m//100)%10
m4= m//1000

nr=n1+n2+n3+n4
mr=m1+m2+m3+m4
if nr==mr:
    print (n, "y", m, "si son familia")
else:
    print (n, "y", m, "no son familia")

    
