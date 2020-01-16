from sys import stdin
def primercaso():
    a=int(stdin.readline().strip())
    b=int(stdin.readline().strip())
    c=int(stdin.readline().strip())
    d=int(stdin.readline().strip())
    if a>b:
        b=b*-1
    if b>a:
        a=a*-1
    print(80+((b-a))+40+((c-d))+((d-c)))
primercaso()
