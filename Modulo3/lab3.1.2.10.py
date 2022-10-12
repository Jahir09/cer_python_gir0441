'''
Descripcion: Funcion For
Autor: Casas Espínola Jahir Artemio
Fecha: 27 de sep del 2022
'''

userWord = None

userWord = input("Ingrese una palabra: ")
userWord = userWord.upper()

for letra in userWord:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        print(letra)