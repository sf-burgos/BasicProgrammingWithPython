from sys import stdin
n= int(stdin.readline().strip())        

n1= n%10
n2= (n//10)%10
n3= (n//100)%10
n4= n//1000

if n1==n2==n3==n4:
    print (n1)
elif n1>=n2 and n1>=n3 and n1>=n4:
    print (n1)
elif n2>=n1 and n2>=n3 and n2>=n4:
    print (n2)
elif n3>=n2 and n3>=n1 and n3>=n4:
     print (n3)
elif n4>=n2 and n4>=n3 and n4>=n1:
    print (n4)    
