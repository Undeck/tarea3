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
for palabra in dic:
    if len(palabra) == 5:
        if palabra[0] == 'y' and palabra[1] == 'e' and palabra[2] == 'v' and palabra[3] == 'r' and palabra[4] == 'z':
            c = c + 1
            print(palabra)