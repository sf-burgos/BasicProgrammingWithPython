from sys import stdin
n=str(stdin.readline().strip())
def palabra(n):
    con=0
    lista=["A" , "B" ,  "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" , "Ñ" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z"]
    for i in n:
        if i in lista:
            con+=1
        else:
            con+=0
    print(con+1)
palabra(n)
