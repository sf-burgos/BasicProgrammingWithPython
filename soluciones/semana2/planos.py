from sys import stdin
x1=float(stdin.readline().strip())
y1=float(stdin.readline().strip())
x2=float(stdin.readline().strip())
y2=float(stdin.readline().strip())
l=str(stdin.readline().strip())
x=float(stdin.readline().strip())
y=float(stdin.readline().strip())
if x1>x2:
    b=x1
    a=x2
else:
    b=x2
    a=x1
if y1>y2:
    d=y1
    c=y2
else:
    d=y2
    c=y1
trat=((x>a and x<b)and(y>c and y<d))
if trat==True:
    print("Point is contained in figure")
else:
    print("Point is not contained in figure")
