from sys import stdin
"""Pre: ninguna
POS: permitira crear un usuario para crear su propio usuario y guardar informacion en su cuenta """
def registro():

    print("Porfavor ingrese una de las opciones:")
    print("1. Ingresar a mi cuenta")
    print("2. Deseo 'REGISTRARME'")
    #z=str(input("Porfavor ingrese una de las opciones: 1.su nombre de usuario. 2. 'REGISTRARSE'"))
    #como meter un enter en una impresion
    z=str(input())
    z=z.lower()
    
    if z=="1":
        w=[]
        nombre=str(input("porfavor, ingrese su nombre de usuario: "))
       
        contraseña=str(input("porfavor, ingrese su contraseña, recuerde que su contraseña solo tendra 4 digitos: "))
        salida(nombre+"\n",1)
        u=open(str(nombre)+str(".txt"),"w")
        w.append(" ")
        w=u.readlines()
        print(w)
        c=w[1]
        if contraseña!=c:
            print("contraseña incorrecta, intentelo de nuevo")
            registro()
        u.close
        return no(nombre)
        
    elif z=="2":
        nombre=str(input("porfavor, ingrese su nombre de usuario"))
        salida(nombre+"\n",0)
        c=open(nombre+str(".txt"),"w")
        contraseña=str(input("porfavor, ingrese su contraseña"))
        c.write(nombre+"\n")
        c.write(contraseña+"\n")
        c.close()
        
        u=open("usuarios"+str(".txt"),"a")
        u.write(nombre+"\n")
        u.close()
        
    else:
        print("Opcion incorrecta,intentelo de nuevo")
        print("________________________________________________________")
        registro()
"""pre: un nombre de usuario + "\n"
pos: revisar si el nombre de usuario ya se encuentra en uso"""
def salida(n,m):
    u=open("usuarios"+str(".txt"),"r")
    x=u.readlines()
    
    print(x,"hola")
    if n in x:
        if m==0:
            print("nombre de usuario en uso, porfavor intentelo de nuevo")
            registro()
def no(n):
    return n
