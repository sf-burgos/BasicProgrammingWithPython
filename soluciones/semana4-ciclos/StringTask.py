from sys import stdin
def task(n):
    for voc in n:
        if voc=="a" or  voc=="e" or  voc=="i" or  voc=="o" or  voc=="u" or voc=="y":

            n=n.replace(voc,"")
            
    z=""
    pot=n.split
    for voc2 in n:
        z=z+"."+str(voc2)
    print(z)
def main():
    n=stdin.readline().strip()
    while n!="":
        n=n.lower()
        task(n)
        n=stdin.readline().strip()

main()
