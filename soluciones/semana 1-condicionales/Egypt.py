from sys import stdin
n= int(stdin.readline().strip())        
n1= int(stdin.readline().strip())
n2= int(stdin.readline().strip())

if n**2+n1**2==n2**2 or n1**2+n2**2==n**2 or n**2+n2**2==n1**2:
    print ("right")
else:
    print ("wrong")
