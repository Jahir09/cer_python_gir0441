'''
Descripcion: Utilizar la funcion for
Autor: Casas Espínola Jahir Artemio
Fecha: 27 de sep del 2022
'''


palabraSinVocal = ""
userWord = ""

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
        palabraSinVocal += letra

print(palabraSinVocal)