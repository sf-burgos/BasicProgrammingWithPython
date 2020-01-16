from math import *
"""#entradaPre:ninguna
Pos: input por shell permitira el ingreso de cualquier funcion trignometrica de la forma y=af(bx+-c)+-d con la cual evaluaremos la funcion del inicio a x y
de x hasta el final de la entrada. lo anterior lo retornara como parte1 y parte2"""
def entrada():
     funcion=[str(xx)for xx in input("INGRESA LA FUNCION QUE QUIERES GRAFICAR  ").strip().split('x')]
     parte1=funcion[0]
     parte2=funcion[1]
     if 'sec' in parte1:
          parte1=parte1.replace('sec','1/sin')
     if 'csc' in parte1:
          parte1=parte1.replace('csc','1/cos')
     if 'cot' in parte1:
          parte1=parte1.replace('cot','1/tan')
     if 'sen' in parte1:
          parte1=parte1.replace('sen','sin')
     
     return parte1,parte2    
'''                
     if '*' in parte1:
          b=parte1.split('*')
          amplitud=b[0]
          c=b[1].split('(')
          periodo=c[1]
          if amplitud=='':
               amplitud=1
          if periodo=='':
               periodo='2*pi'
          else:
               periodo=eval(str('2*pi')+'/'+str(periodo))
               amplitud=1
      
     if 'tan' in parte1:
          b=parte1.split('*')
          amplitud=b[0]
          c=b[1].split('(')
          periodo=c[1]
          if amplitud=='':
               amplitud=1
          if periodo=='':
               h='π'
               periodo='pi'
          
          else:
               periodo=eval(str('pi')+'/'+str(periodo))
               amplitud=1
     
'''               
     
    
    

            

