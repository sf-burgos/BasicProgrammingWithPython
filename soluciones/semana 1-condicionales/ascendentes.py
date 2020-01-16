from sys import stdin

n1= int(stdin.readline().strip())        
n2= int(stdin.readline().strip())
n3= int(stdin.readline().strip())
 
def tomar(n1,n2,n3):
  if n1<=n2 and n2<=n3:
    print (n1,n2,n3)
  elif n2<=n1 and n1<=n3:
    print (n2,n1,n3)
  elif n3<=n2 and n2<=n1:
    print (n3,n2,n1)
  elif n3<=n1 and n1<=n2:
    print (n3,n1,n2)
  elif n2<=n3 and n3<=n1:
    print (n2,n3,n1)
  elif n1<=n3 and n3<=n2:
    print(n1,n3,n2)

tomar (n1,n2,n3)
