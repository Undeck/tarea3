'''def cargaCifrado():
    archivo = open('cifrado.txt', 'r')
    renglon = archivo.readline()
    return renglon
cifrado = cargaCifrado()
histo = {}
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
for e in alfabeto:
    histo[e] = 0
print(histo)
print('-------------------')
for letra in cifrado:
    if letra in alfabeto:
        histo[letra] += 1
print(histo)'''

