from sys import stdin
def main():
    lista=[]
    entrada=[int(xx) for xx in stdin.readline().strip().split(" ")]
    num1=entrada[0]
    num2=entrada[1]
    num3=entrada[2]
    num4=entrada[3]
    num5=entrada[4]
    if primercaso(num1,num2)==True:
        print("Possible",1)
        return
    elif segundocaso(num1,num2,num3)==True:
        print("Possible",2)
        return
    elif tercercaso(num1,num2,num3,num4)==True:
        print("Possible",3)
        return
    elif cuartocaso(num1,num2,num3,num4,num5)==True:
        print("Possible",4)
        return
    else:
        (print("Impossible"))
def primercaso (num1,num2):
    a=num1+num2
    b=num1-num2
    c=num1*num2
    if a==23 or b==23 or c==23:
        return True
def segundocaso (num1,num2,num3):
    if num1+num2+num3==23 or num1-num2+num3==23 or num1*num2+num3==23 or num1+num2-num3==23 or num1+num2-num3==23 or num1+num2-num3==23 or num1+num2*num3==23 or num1+num2*num3==2 or num1+num2*num3==23:
        return True
    else:
        return False
def tercercaso(num1,num2,num3,num4):
    if num1+num2+num3+num4==23 or num1+num2+num3-num4==23 or num1+num2+num3*num4==23 or num1-num2+num3+num4==23 or num1-num2+num3-num4==23 or num1-num2+num3*num4==23 or num1*num2+num3+num4==23 or num1*num2+num3-num4==23 or num1*num2+num3*num4==23 or num1+num2-num3+num4==23 or num1+num2-num3-num4==23 or num1+num2-num3*num4==23 or num1+num2-num3+num4==23 or num1+num2-num3-num4==23 or num1+num2-num3*num4==23 or num1+num2-num3+num4==23 or num1+num2-num3-num4==23 or num1+num2-num3*num4==23 or num1+num2*num3+num4==23 or num1+num2*num3-num4==23 or num1+num2*num3*num4==23 or num1+num2*num3+num4==23 or num1+num2*num3-num4==23 or num1+num2*num3*num4==23 or num1+num2*num3+num4==23 or num1+num2*num3-num4==23 or num1+num2*num3*num4==23:
        return True
def cuartocaso(num1,num2,num3,num4,num5):
    if num1+num2+num3+num4+num5==23 or num1-num2-num3-num4-num5==23 or num1*num2*num3*num4*num5==23:
        return True
main()
