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

    for p in dic:
        if len(p) == 8 and p[1] in posO and p[-1] in posD and p[1] == p[5] and p[3] == p[-1] and p[2] == p[6] and p[0] == 'd':
            c = c + 1
            print(p)



def descifraSustituye(cifrado, llave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    descifrado = ''
    for letra in cifrado:
        if letra in alfabeto:
            posicion = llave.index(letra)
            descifrado += alfabeto[posicion]
        else:
            descifrado += letra
    return descifrado
alfabeto_original = 'abcdefghijklmnopqrstuvwxyz'
llave = 'rhkqvsyplXxbidoaXeuzcXgXtX'
mensaje_cifrado = "l prq r yevrz gvvxvdq. od selqrt rszvedood, l sldlupvq goex rz 5 ai. l gvdz poiv rdq zoox r upogve. zpvd l gvdz zo uvv r kocabv os it selvdqu rz r hre qogdzogd."
mensaje_descifrado = descifraSustituye(mensaje_cifrado, llave)
print(mensaje_descifrado)

