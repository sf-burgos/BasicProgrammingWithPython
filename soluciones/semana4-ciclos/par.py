from sys import stdin

def par(n):
     if n%2==0:
          return True
     else:
          return False
def contador(lista):
     p=0
     o=0
     for limon in lista:
          r=par(limon)
          if r== True:
               p=p+1
          else:
               o=o+1
     print ("Pares: "+str(p)+" Impares: "+str(o))
     
def main ():
     n=int(stdin.readline().strip())
     c=1
     while n!=0:
          y=[int(arr_temp) for arr_temp in stdin.readline().strip().split(" ")]
          print ("Lista"+str(c)+":")
          contador(y)
          n=n-1
          c=c+1
main()
