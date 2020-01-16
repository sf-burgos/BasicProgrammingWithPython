from sys import stdin
a=int(stdin.readline())
b=int(stdin.readline())
c=int(stdin.readline())

n1=a+b+c
n2=a*b*c
n3=(a+b)*c
n4=a*(b+c)
n5=a+(b*c)
n6=(a*b)+c

if n1>=n2 and n1>=n3 and n1>=n4 and n1>=n5 and n1>=n6:  
  print (n1)
elif n2>=n1 and n2>=n3 and n2>=n4 and n2>=n5 and n2>=n6:  
  print (n2)
elif n3>=n1 and n3>=n2 and n3>=n4 and n3>=n5 and n3>=n6:  
  print (n3)
elif n4>=n2 and n4>=n3 and n4>=n1 and n4>=n5 and n4>=n6:  
  print (n4)
elif n5>=n2 and n5>=n3 and n5>=n4 and n5>=n1 and n5>=n6:  
  print (n5)
elif n6>=n2 and n6>=n3 and n6>=n4 and n6>=n5 and n6>=n1:  
  print (n6)  
