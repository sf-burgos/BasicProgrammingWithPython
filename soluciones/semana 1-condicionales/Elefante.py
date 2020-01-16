from sys import stdin
d= int(stdin.readline().strip())

if d%5==0:
   print(d//5)
elif (d%5)%4==0:
   print(d//5+d%5//4)
elif ((d%5)%4)%3==0:
   print(d//5+d%5//4+((d%5)%4)//3)
elif ((((d%5)%4)%3)%2)==0:
   print ((d//5+d%5//4)+(((d%5)%4)//3)+((((d%5)%4)%3)//2))
elif (((((d%5)%4)%3)%2)%1)==0:
    print((d//5+d%5//4)+(((d%5)%4)//3)+((((d%5)%4)%3//2)+((((d%5)%4)%3)%2)//1))
