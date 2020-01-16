from sys import stdin
def main():
    lista_datos_iniciales=[]
    n=int(stdin.readline().strip())
    datos=str(stdin.readline().strip())
    
    for i in range(n*10):
        datos=float(datos)
        lista_datos_iniciales.append(datos)
        datos=str(stdin.readline().strip())
    numero_datos=len(lista_datos_iniciales)
##  EN LA MEDIA ESTAN LOS VALORES ATIPICOS
    sumatoria=0
    
    for i in lista_datos_iniciales:
        sumatoria+=i
    promedio=sumatoria/numero_datos
    sumatoria_datos_2=0
##  EN LA MEDIA ESTAN LOS VALORES ATIPICOS
    
    for i in lista_datos_iniciales:
        sumatoria_datos_2+=(i-promedio)**2
    interna=(sumatoria_datos_2/(numero_datos-1))
    desviacion=interna**0.5
    lista_sin_valores_atipicos=[]
    
    for i in lista_datos_iniciales:
        if i<(promedio+desviacion) and i>(promedio-desviacion):
            lista_sin_valores_atipicos.append(i)
    promedio_final=0
    
    for i in lista_sin_valores_atipicos:
        promedio_final=promedio_final+i
    l=len(lista_sin_valores_atipicos)
    print("La temperatura del crudo es:",round(promedio_final/l,2),)
main()
