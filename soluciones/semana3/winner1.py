from sys import stdin
def winner (n1,n2,n3,n4,n5,op1,op2,op3,op4):
    #print(op1,op2,op3,op4)
    if op1==1:
        res=n1+n2
    elif op1==2:
        res=n1-n2
    else:
        res=n1*n2
    #bloque2
    if op2==1:
        res=res+n3
    elif op2==2:
        res=res-n3
    else:
        res=res*n3
    #bloque3
    if op3==1:
        res=res+n4
    elif op3==2:
            res=res-n4
    else:
        res=res*n4
    
    #bloque4
    if op4==1:
        res=res+n5
    elif op4==2:
        res=res-n5
    else:
        res=res*n5

    if res==23:
        return True
    else:
        if op1<3:
            return winner(n1,n2,n3,n4,n5,op1+1,op2,op3,op4)
        else:
            if op2<3:
                return winner(n1,n2,n3,n4,n5,1,op2+1,op3,op4)
            else:
                if op3<3:
                    return winner(n1,n2,n3,n4,n5,1,1,op3+1,op4)
                else:
                    if op4<3:
                        return winner(n1,n2,n3,n4,n5,1,1,1,op4+1)
                    else:
                        #print("Imposible")
                        return False
def main():
    entrada=[int (xx) for xx in stdin.readline().strip().split(" ")]
    n1=entrada[0]
    n2=entrada[1]
    n3=entrada[2]
    n4=entrada[3]
    n5=entrada[4]
    if (winner (float(n1),float(n2),float(n3),float(n4),float(n5),1,1,1,1)):
        print("Possible")
    else:
        print("Impossible")
main()
