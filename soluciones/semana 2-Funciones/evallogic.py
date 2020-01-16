from sys import stdin
def evallogic ():
    proposicion=stdin.readline().strip()
    p=stdin.readline().strip()
    q=stdin.readline().strip()
    r=stdin.readline().strip()
    s=stdin.readline().strip()
    proposicion=proposicion.replace("r",  " i ")
    proposicion=proposicion.replace("s",  " ñ ")
    
    proposicion=proposicion.replace("^",  " and ")
    proposicion=proposicion.replace("v",  " or ")
    proposicion=proposicion.replace("-",  " not ")
  
    
    if p=="T":
        proposicion=proposicion.replace("p", "True") 
    elif p=="F":
        proposicion=proposicion.replace("p", "False")
    if q=="T":
        proposicion=proposicion.replace("q", "True")
    elif q=="F":
        proposicion=proposicion.replace("q", "False")
    if s=="T":
        proposicion=proposicion.replace("ñ", "True")
    elif s=="F":
        proposicion=proposicion.replace("ñ", "False")
    if r=="T":
        proposicion=proposicion.replace("i", "True")
    elif r=="F":
        proposicion=proposicion.replace("i", "False")

    print (eval(proposicion)) 
evallogic()

