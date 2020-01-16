from sys import stdin
##idioma=(stdin.readline().strip())

def xxxx(idioma):
    if idioma=="HELLO":
        return("ENGLISH")
    elif idioma=="HOLA":
        return ("SPANISH")
    elif idioma=="HALLO":
        return "GERMAN"
    elif idioma=="BONJOUR":
        return "FRENCH"
    elif idioma=="CIAO":
        return "ITALIAN"
    elif idioma=="ZDRAVSTVUJTE":
        return "RUSSIAN"
    else:
        return "UNKNOWN"

def main():
    c=1
    idioma=(stdin.readline().strip())
    while idioma!="#":
        xxxx(idioma)
        print("Case",str(c)+":",xxxx(idioma))
        c+=1
        idioma=(stdin.readline().strip())
main()
