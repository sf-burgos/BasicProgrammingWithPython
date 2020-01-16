from sys import stdin
def main():
    diferencia=int(stdin.readline().strip())
    while diferencia:
        diferencia=int(diferencia)
        rita=int(stdin.readline().strip())
        theo=int(stdin.readline().strip())
        velastotal=rita+theo
        sumartodo=0
        inicioniña=4
        inicioniño=3
        niña=0
        niño=0
        while sumartodo<velastotal:
            if inicioniña-diferencia<inicioniño:
                niña+=inicioniña
                sumartodo+=inicioniña
                inicioniña+=1
            else:
                niña+=inicioniña
                niño+=inicioniño
                sumartodo+=inicioniña+inicioniño
                inicioniña+=1
                inicioniño+=1
        print(rita-niña)
        diferencia=stdin.readline().strip() 

main()
            
