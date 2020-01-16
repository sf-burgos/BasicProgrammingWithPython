from sys import stdin
n=abs(int(stdin.readline().strip()))
m=abs(int(stdin.readline().strip()))
l=int(stdin.readline().strip())
def distance():
    if (n+m)==l:
        print ("Yes")
    elif (n+m)>l:
        print ("No")
    elif (n+m)<l:
        if((((n+m)-l)%2)==0):
            print("Yes")
        else: 
            print ("No")
distance()
