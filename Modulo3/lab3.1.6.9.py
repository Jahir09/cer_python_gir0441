'''
Descripcion: listas y for 
Autor: Casas Espínola Jahir Artemio
Fecha: 27 de sep del 2022
'''

miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

listaTemp = []

for numero in miLista:
    if numero not in listaTemp:
        listaTemp.append(numero)

miLista = listaTemp[:]

print("La lista solo con elementos únicos:")
print(miLista)