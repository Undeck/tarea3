def cargaPalabras(archivo):
    renglon = archivo.readline()
    palabras = renglon.split()
    return palabras

def cargaCifrado():
    archivo = open('cifrado.txt', 'r')
    renglon = archivo.readline()
    archivo.close()
    return renglon

def cifraCesar(cadena, llave):
    if llave < 0:
        llave = 26 - llave
    cadena = cadena.lower()
    nuevaCadena = ""
    alfabeto = 'abcdefghijkimnoporscuywayz'
    for letra in cadena:
        if letra in alfabeto:
            posicionLetra = alfabeto.find(letra)
            nuevaCadena = nuevaCadena + alfabeto[((posicionLetra + llave) % 26)]
        else:
            nuevaCadena = nuevaCadena + letra
    return nuevaCadena

def descifraCesar(cadena, llave):
    return cifraCesar(cadena, 26 - llave)

def getAciertos(listaPalabras, diccionario):
    numAciertos = 0
    for pal in listaPalabras:
        if pal in diccionario:
            numAciertos = numAciertos + 1
    return numAciertos

# Definición de posO y posD
posA="abcdefghijklmnopqrstuvwxyz"
posB="abcdefghijklmnopqrstuvwxyz"
posC="abcdefghijklmnopqrstuvwxyz"
posD="abcdefghijklmnopqrstuvwxyz"
posE="abcdefghijklmnopqrstuvwxyz"
posG="abcdefghijklmnopqrstuvwxyz"
posH="abcdefghijklmnopqrstuvwxyz"
posI="abcdefghijklmnopqrstuvwxyz"
posK="abcdefghijklmnopqrstuvwxyz"
posL="abcdefghijklmnopqrstuvwxyz"
posO="abcdefghijklmnopqrstuvwxyz"
posP="abcdefghijklmnopqrstuvwxyz"
posQ="abcdefghijklmnopqrstuvwxyz"
posR="abcdefghijklmnopqrstuvwxyz"
posS="abcdefghijklmnopqrstuvwxyz"
posT="abcdefghijklmnopqrstuvwxyz"
posU="abcdefghijklmnopqrstuvwxyz"
posV="abcdefghijklmnopqrstuvwxyz"
posX="abcdefghijklmnopqrstuvwxyz"
posY="abcdefghijklmnopqrstuvwxyz"
posZ="abcdefghijklmnopqrstuvwxyz"


# Abre el archivo 'words.txt' y carga las palabras.
with open('words.txt', 'r') as archivo:
    dic = cargaPalabras(archivo)
    c = 0

#probando con qogdzogd.
for p in dic:
    if len(p)==8:
        if p[1]==p[5] and p[3]==p[-1] and p[2]==p[6]:
            if p[0]== 'd' and p[1] in posO and p[-1] in posD:
                    c = c + 1
                    print(p)
#probando con rszvedood.
for p in dic:
    if len(p)==9:
        if p[5]==p[-1] and p[6]==p[7]:
            if p[6] in posO and p[-1] in posD:
                if p[0] in posR and p[1] in posS and p[3] in posV: 
                    c = c + 1
                    print(p)
# probando con gvvxvdq
for p in dic:
    if len(p)==7:
        if p[0] in posG and p[1] in posV:
            if p[1]==p[2] and p[2]== p[4]:
                if p[-1] in posQ and p[-2] in posD:
                    c = c + 1
                    print(p)
# probando con prq  Xad
for p in dic:
    if len(p)==3:
        if p[1:]=='ad':
            c = c + 1
            print(p)
# probando con selqrt
for p in dic:
    if len(p)==6:
        if p[:2]=='fr' and p[3:5]=='da':
            c = c + 1
            print(p)





