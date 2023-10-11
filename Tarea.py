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