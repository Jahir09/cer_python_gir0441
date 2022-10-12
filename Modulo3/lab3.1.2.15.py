'''
Descripcion: Funcion if
Autor: Casas Espínola Jahir Artemio
Fecha: 27 de sep del 2022
'''

numero = int(input("Ingrese un número: "))
estaResuelto = False
pasos = 0

if numero >= 1:
    while estaResuelto == False:
        if numero != 1:
            if (numero % 2) == 0:
                numero //= 2
            else:
                numero = (3 * numero) + 1

            pasos += 1
            print(numero)
        else:
            estaResuelto = True

print("pasos =", pasos)