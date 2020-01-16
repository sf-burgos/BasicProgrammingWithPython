from sys import stdin
def main():
    entrada=str(stdin.readline().strip())
    while entrada!="":
        b=""
        for i in entrada:
            if i=="A" or i=="B" or i=="C":
                b+="2"
            elif i=="D" or i=="E" or i=="F":
                b+="3"
            elif i=="G" or i=="H" or i=="I":
                b+="4"
            elif i=="J" or i=="K" or i=="L":
                b+="5"
            elif i=="M" or i=="N" or i=="O":
                b+="6"
            elif i=="P" or i=="Q" or i=="R" or i=="S":
                b+="7"
            elif i=="T" or i=="U" or i=="V":
                b+="8"
            elif i=="W" or i=="X" or i=="Y" or i=="Z":
                b+="9"
            else:
                b+=i
        print(b)
        entrada=str(stdin.readline().strip())
main()
