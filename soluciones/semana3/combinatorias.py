from sys import stdin
def potencia(c):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

def imprime_ordenado(c,lista,entrada):
    """Imprime en la salida estándar todos los
       subconjuntos del conjunto c (una lista de
       listas) ordenados primero por tamaño y
       luego lexicográficamente. Cada subconjunto
       se imprime en su propia línea. Los
       elementos de los subconjuntos deben ser
       comparables entre sí, de otra forma puede
       ocurrir un TypeError.
    """
    for e in sorted(c, key=lambda s: (len(s), s)):
        prueba=[]
        prueba.append(e)
        for i in range(len(prueba)):
            if 
    
        
    return lista 
def main():
    lista=[]
    entrada=[str(xx) for xx in stdin.readline().strip().split(" ")]
    num1=entrada[0]
    num2=entrada[1]
    num3=entrada[2]
    num4=entrada[3]
    num5=entrada[4]
    print(imprime_ordenado(potencia(["+","*","-",num1,num2,num3,num4,num5]),lista,entrada))
    
main()
