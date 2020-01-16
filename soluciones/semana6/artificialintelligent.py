from sys import stdin
def main():
    n=int(stdin.readline().strip())
    for i in range (n):
        entrada=[str(x) for x in stdin.readline().strip().split("=")]

        dato1=entrada[1]
        dato2=entrada[2]
        
        ecuacion=[0,0,0]
        
        if "A" in dato2:
            dato2=dato2[:dato2.index("A")]
            ecuacion[2]=dato2
        elif "V" in dato2:
            dato2=dato2[:dato2.index("V")]
            ecuacion[1]=dato2
        elif "W" in dato2:
            dato2=dato2[:dato2.index("W")]
            ecuacion[0]=dato2
            
        if "A" in dato1:
            dato1=dato1[:dato1.index("A")]
            ecuacion[2]=dato1
        elif "V" in dato1:
            dato1=dato1[:dato1.index("V")]
            ecuacion[1]=dato1
        elif "W" in dato1:
            dato1=dato1[:dato1.index("W")]
            ecuacion[0]=dato1

        
        if "M" in str(ecuacion[0]):
            a=str(ecuacion[0])
            z=a.index("M")
            dato1=float(a[:z])*(10**6)
            ecuacion[0]=dato1
        if "k" in str(ecuacion[0]):
            a=str(ecuacion[0])
            z=a.index("k")
            dato1=float(a[:z])*(10**3)
            ecuacion[0]=dato1
        if "m" in str(ecuacion[0]):
            a=str(ecuacion[0])
            z=a.index("m")
            dato1=float(a[:z])*(10**-3)
            ecuacion[0]=dato1


        if "M" in str(ecuacion[1]):
            a=str(ecuacion[1])
            z=a.index("M")
            dato1=float(a[:z])*(10**6)
            ecuacion[1]=dato1
        if "k" in str(ecuacion[1]):
            a=str(ecuacion[1])
            z=a.index("k")
            dato1=float(a[:z])*(10**3)
            ecuacion[1]=dato1
        if "m" in str(ecuacion[1]):
            a=str(ecuacion[1])
            z=a.index("m")
            dato1=float(a[:z])*(10**-3)
            ecuacion[1]=dato1

        if "M" in str(ecuacion[2]):
            a=str(ecuacion[2])
            z=a.index("M")
            dato1=float(a[:z])*(10**6)
            ecuacion[2]=dato1
        if "k" in str(ecuacion[2]):
            a=str(ecuacion[2])
            z=a.index("k")
            dato1=float(a[:z])*(10**3)
            ecuacion[2]=dato1
        if "m" in str(ecuacion[2]):
            a=str(ecuacion[2])
            z=a.index("m")
            dato1=float(a[:z])*(10**-3)
            ecuacion[2]=dato1


        print("Problem #"+str(i+1))
        if ecuacion[0]==0:
            a=float(ecuacion[1])*float(ecuacion[2])
            a="%.2f" % a
            print("P="+str(a)+str("W"))
    
        if ecuacion[1]==0:
            a=float(ecuacion[0])/float(ecuacion[2])
            a="%.2f" % a
            print("U="+str(a)+str("V"))

            
        if ecuacion[2]==0:
            a=float(ecuacion[0])/float(ecuacion[1])
            a="%.2f" % a
            print("I="+str(a)+str("A"))
        print("")

        
main()
