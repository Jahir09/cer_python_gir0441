'''
Descripcion: Utilizar la Funcion if and else con años
Nombre: Casas Espínola Jahir Artemio 
Fecha: 29/sept/22
'''

año = int(input("Introduzca un año:"))

divisibleEntre_4 = año % 4
divisibleEntre_100 = año % 100
divisibleEntre_400 = año % 400

if año >= 1582:
    if divisibleEntre_4 != 0:
        print("Año común")
    elif divisibleEntre_100 != 0:
        print("Año bisiesto")
    elif divisibleEntre_400 != 0:
        print("Año común")
    else:
        print("Año bisiesto")
else:
    print("No dentro del período del calendario gregoriano")